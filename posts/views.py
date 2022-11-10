from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Posts
from .forms import PostForm 
from django.forms import forms

def index(request):
    # if the method is POST
    if request.method == 'POST':
          form = PostForm(request.POST, request.FILES)
          #if the form is valid
          if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect ('/')
          else:
            # No, show Error
      
            return HttpResponseRedirect(form.errors.as_json())  # type: ignore
      #Get all posts, limit = 20
    posts = Posts.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    # Show 
    return render ( request, 'posts.html',
                        {'posts': posts})

# def delete(request, post_id):  # type: ignore
#     output = 'POST ID is' + str(post_id)
#     return HttpResponse(output)

def delete(request, post_id):
    post = Posts.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def likes(request, id):
    likedtweet = Posts.objects.get(id = id)
    likedtweet.like_count += 1
    likedtweet.save()
    return HttpResponseRedirect("/")

def edit(request, post_id):
  posts = Posts.objects.get(id=post_id)
  # if request.method == "GET":
  #   posts = Posts.objects.get(id=id)
    
  if request.method == "POST":
    # editposts = Posts.objects.get(id = id)
    form = PostForm(request.POST, request.FILES, instance=posts)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/")
    else:
      return HttpResponse("not valid")
  form = PostForm
  return render(request, "edit.html", {"posts": posts})

