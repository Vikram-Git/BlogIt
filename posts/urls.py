from django.urls import re_path, include
from . import views

app_name = 'posts'

urlpatterns = [

    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^category/$', views.category, name='category'),
    re_path(r'^trending/$', views.trending_post, name='trending_post'),
    re_path(r'^search/$', views.search_query, name='search_query'),
    re_path(r'^(?P<post_slug>([\w-]+))/$', views.post_detail, name='post_detail'),
    re_path(r'^tag/(?P<category_title>([\w]+))/$', views.category_list, name="category_list"),

]


