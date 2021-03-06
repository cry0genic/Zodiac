from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/update/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    path("user_posts/<int:pk>", views.user_posts, name="user-posts-list"),
    
]
