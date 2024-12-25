from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def index(request):
    blogs = Post.objects.all().order_by('-last_update')
    return render(request, "blog/index.html", {
        'blogs': blogs,
    })

def view_blog(request, id):
    blog = Post.objects.get(id=id)
    return render(request, "blog/view_blog.html", {
        'blog': blog,
    })

def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.image:
                post.image = 'defaults/default-thumbnail.png'
            post.save()
        else:
            print(form.errors)
        return redirect('index')

    return render(request, "blog/create_post.html", {
        'form': form,
        'mode': 'create'
    })

def edit_post(request, id):
    blog = Post.objects.get(id=id)
    form = PostForm(instance=blog)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.image:
                post.image = 'defaults/default-thumbnail.png'
            post.save()
        return redirect('index')

    return render(request, "blog/create_post.html", {
        'form': form,
        'mode': 'edit'
    })

def delete_post(request, id):
    blog = Post.objects.get(id=id)
    blog.delete()
    return redirect('index')