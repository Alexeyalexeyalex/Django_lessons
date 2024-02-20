from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author_form, name='author_form'),
    path('post/', views.posts_form, name='posts_form'),
    path('posts/<int:author_id>/', views.posts, name='posts'),
    path('posts/post/<int:post_id>/', views.author_post, name='author_post'),

]