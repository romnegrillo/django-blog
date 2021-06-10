from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import NewPostForm, EditPostForm
from django.contrib import messages
from django.http import HttpResponseForbidden

# Sample hardcoded.
posts = [
     {
        "author": "Gusion",
        "title": "Gusion Quotes",
        "content": "The perfect combination of might and magic.",
        "date_posted": "June 06, 2021",
     },
     {
        "author": "Zilong",
        "title": "Zilong Quotes",
        "content": "Your whole body is a weak spot.",
        "date_posted": "June 06, 2021",
     },
 ]


def home(request):

    # Actual from the database.
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})

def about(request):

    return render(request, "blog/about.html")

def post(request, post_id):

    # Get the post_id parameter from the urls
    # then query a post with that id then pass
    # it to the render function to display
    # that particular post.
    post = Post.objects.get(pk = post_id)
    return render(request, "blog/post.html", {"post": post})

def create_post(request):

    if request.method == "POST":
        form = NewPostForm(request.POST)
        form.instance.author = request.user
           
        if form.is_valid():
            form.save()
            messages.success(request, "Your content has been posted.")
            return redirect("blog-home")

    else:
        form = NewPostForm()
        form.instance.author = request.user

    return render(request, "blog/new.html", {"form": form})

def edit_post(request, post_id):

    if request.method == "POST":
        # Get the current post first base on the ID.
        post = Post.objects.get(pk = post_id)

        # Check if the current user is also
        # the user from the post. If not return
        # forbidden error.
        if post.author != request.user:
            return HttpResponseForbidden("<h1>403 Forbidden</h1>")


        # This will automaticallt set the fields of
        # that particular post.
        form = EditPostForm(request.POST, instance = post)
           
        if form.is_valid():
            form.save()
            messages.success(request, "Your content has been updated.")
            return redirect("blog-home")

    else:
         # Get the current post first base on the ID.
        post = Post.objects.get(pk = post_id)

        # Check if the current user is also
        # the user from the post. If not return
        # forbidden error.
        if post.author != request.user:
            return HttpResponseForbidden("<h1>403 Forbidden</h1>")

        # Create the form with that instance post.
        # This will automaticallt set the fields of
        # that particular post.
        form = EditPostForm(instance = post)
      
        
    return render(request, "blog/edit.html", {"form": form})


def delete_post(request, post_id):

    # Get the current post first base on the ID.
    post = Post.objects.get(pk = post_id)

    if post.author != request.user:
        return HttpResponseForbidden("<h1>403 Forbidden</h1>")

    if request.POST.get("delete-post-btn"):
        #print("Delete button pressed.")
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect("blog-home")
    else:
        #print("Delete button not pressed.")
        pass


    return render(request, "blog/delete.html", {"post": post})

