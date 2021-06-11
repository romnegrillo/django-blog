from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "blog-home"),
    path('post/<int:post_id>/', views.post, name = "blog-post"),
    path('post/new/', views.create_post, name = "blog-new"),
    path('post/user/<int:user_id>', views.post_user, name = "blog-post-user"),
    path('post/edit/<int:post_id>/', views.edit_post, name = "blog-edit"),
    path('post/delete/<int:post_id>/', views.delete_post, name = "blog-delete"),
    path('about/', views.about, name = "blog-about"),
]
