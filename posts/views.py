import datetime

from dateutil import relativedelta

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage
from .models import Post, Visitor, Category

from django.db.models import Count, Q


def post_list(request):
    published_post = Post.objects.filter(publish=True)

    paginator = Paginator(published_post, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    # Trending post algorithm
    posts_visit_count = Visitor.objects.filter(post__in=published_post) \
        .values('post').annotate(visits=Count('post__id')).order_by('-visits')

    trending_posts_id = [post['post'] for post in posts_visit_count]

    date_now = datetime.datetime.now()
    date_since = date_now - relativedelta.relativedelta(months=3)

    trend_post = published_post.filter(pk__in=trending_posts_id) \
        .filter(updated__date__range=[date_since, date_now])[:5]

    context = {'posts': posts, 'trend_post': trend_post}
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_slug):
    this_post = get_object_or_404(Post, slug=post_slug)
    if not Visitor.objects.filter(post=this_post, ip=request.META['REMOTE_ADDR']):
        visitor_obj = Visitor(post=this_post,
                              ip=request.META['REMOTE_ADDR'])
        visitor_obj.save()

    new_posts = Post.objects.filter(publish=True) \
                    .exclude(slug__icontains=post_slug)[:6]

    # related post algorithm
    tags = [category for category in this_post.category.all()]
    related_posts = Post.objects.filter(category__in=tags) \
                        .exclude(slug__icontains=post_slug)[:6]

    context = {'this_post': this_post,
               'new_posts': new_posts,
               'related_posts': related_posts
               }
    return render(request, 'posts/post_details.html', context)


def category_list(request, category_title):
    category_post = Post.objects.filter(category__title=category_title)
    title = category_title.upper()
    paginator = Paginator(category_post, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts, 'title': title}
    return render(request, 'posts/category_list.html', context)


def trending_post(request):
    published_post = Post.objects.filter(publish=True)

    posts_visit_count = Visitor.objects.filter(post__in=published_post) \
        .values('post').annotate(visits=Count('post__id')).order_by('-visits')

    trending_posts_id = [post['post'] for post in posts_visit_count]

    date_now = datetime.datetime.now()
    date_since = date_now - relativedelta.relativedelta(months=3)

    trend_post = published_post.filter(pk__in=trending_posts_id) \
        .filter(updated__date__range=[date_since, date_now])

    return render(request, 'posts/trending_list.html', {'posts': trend_post})


def search_query(request):
    query = request.GET.get("q")
    published_posts = Post.objects.filter(publish=True)

    search_posts = published_posts.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    ).distinct()

    new_posts = Post.objects.filter(publish=True)[:6]

    return render(request, 'posts/search.html', {'search_posts': search_posts, 'new_posts': new_posts})


def category(request):
    category = Category.objects.all()
    return render(request, 'posts/category.json', {'category': category})

