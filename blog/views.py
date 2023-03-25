from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


post_list = PostListView.as_view()


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day, )

    return render(request, 'blog/post_detail.html', {'post': post})
