from django.shortcuts import render
from blog.models import Post
from blog.models import Category
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, get_list_or_404


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        is_published=True,
        pub_date__lt=now(),
        category__is_published=True,
    )[:5]
    context = {
        'post_list': post_list, }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, pk=pk,
                             category__is_published=True,
                             is_published=True,
                             pub_date__lt=now(),)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = get_list_or_404(Post, category=category,
                                is_published=True,
                                pub_date__lt=now())
    context = {'post_list': post_list, 'category': category}
    return render(request, template, context)
