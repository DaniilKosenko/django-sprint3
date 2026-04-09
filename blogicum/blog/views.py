from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import Post, Category

POSTS_PER_PAGE = 5


def index(request):
    post_list = (Post.objects.with_related_data()
                 .valid_for_display()
                 .recent(POSTS_PER_PAGE))
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post.objects
                             .valid_for_display(),
                             pk=pk)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = (category.posts
                 .published()
                 .not_future())
    if not post_list.exists():
        raise Http404('Постов в данной категории не найдено')
    context = {'post_list': post_list, 'category': category}
    return render(request, 'blog/category.html', context)
