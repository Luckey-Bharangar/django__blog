from django.urls import path,include
# from .views import PostListView, PostDetailView
from .views import PostCreateView,PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    # path('', PostListView.as_view(), name="blog-home"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
   
    path('', views.home_page, name="blog-home"),
    path('post/<int:pk>/', views.detail_page, name="blog-detail"),
    path('about/', views.about_page, name="blog-about"),
    path('post/new/', PostCreateView.as_view(), name="blog-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
]
