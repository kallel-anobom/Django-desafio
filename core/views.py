from django.shortcuts import render

from core.models import Post, Tag

# Create your views here.
def blog_list(request):
  posts = Post.objects.all()
  tags = Tag.objects.all()
  context = {
    'posts': posts,
    'tags': tags,
  }
  return render(request, 'blog/list.html', context)