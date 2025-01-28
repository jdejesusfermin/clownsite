from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'clownsite/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Fetch the post with the given primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'clownsite/post_detail.html', {'post': post})
