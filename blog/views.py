from django.shortcuts import render
# from django.views.generic import ListView, DeleteView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator  import PageNotAnInteger, Paginator, EmptyPage

def home_page(request):

    posts_objs = Post.objects.all().order_by('-date_posted')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_objs, 4)
    try:
        posts_objs = paginator.page(page)
    except PageNotAnInteger:
        posts_objs = paginator.page(1)
    except EmptyPage:
        posts_objs = paginator.page(paginator.num_pages)

    context = {
        'posts': posts_objs
    }
    return render(request, 'blog/home.html', context)


# class PostListView(ListView):
#     model = Post
    # template_name = 'blog/home.html'   # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    

def detail_page(request, pk):
    context = {
        'post': Post.objects.get(pk = pk)
    }
    return render(request, 'blog/post_detail.html', context)


# class PostDetailView(DeleteView):
#     model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about_page(request):
    return render(request, 'blog/about.html', {'title':'About'})

