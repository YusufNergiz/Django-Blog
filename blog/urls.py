from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
       path('', PostListView.as_view(), name='blog-home'),
       path('post/<int:pk>/', PostDetailView.as_view(), name='detail-blog'),
       path('post/new', PostCreateView.as_view(), name='create-blog'),
       path('post/<str:username>', UserPostListView.as_view(), name='users-posts'),
       path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-blog'),
       path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-blog'),
       path('about/', views.about, name='blog-about'),
]