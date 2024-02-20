from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from random import choice, randint
from blog.models import Post, Author, Comment
from .forms import AuthorForm, PostForm, CommentForm


def posts(request, author_id):
    # author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author_id=author_id)
    return render(request, 'blog/posts.html', {'posts':posts})


def author_post(request, post_id):
    posts = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    post = {
        "title": posts.title,
        "pub_date": posts.pub_date,
        "content": posts.content
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(author = data['author'],
                                post = posts,
                                content = data['content'],)
            return redirect('author_post', post_id)
    else:
        form = CommentForm()

    return render(request, 'blog/post.html', {'post':post,'comments':comments, 'form':form})


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_form')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})


def posts_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(title=data['title'],
                                        content=data['content'],
                                        pub_date=data['pub_date'],
                                        author=data['author'],
                                        category=data['category'],
                                        views_count=data['views_count'],
                                        ispublic=data['ispublic'],)
            
            return redirect('posts_form')
    else:
        form = PostForm()
    return render(request, 'blog/author_form.html', {'form': form})