from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "blog-home"),
    path('post/<int:post_id>/', views.post, name = "blog-post"),
    path('post/new/', views.create_post, name = "blog-new"),
    path('post/edit/<int:post_id>/', views.edit_post, name = "blog-edit"),
    path('about/', views.about, name = "blog-about"),
]
