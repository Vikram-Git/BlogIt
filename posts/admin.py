from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class AuthorResource(resources.ModelResource):

    class Meta:
        model = Author

class AuthorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'link']
    search_fields = ['user__username', 'user__email', 'link']
    list_filter = ['user__is_active', 'user__is_staff', 'user__is_superuser']


class PostResource(resources.ModelResource):

    class Meta:
        model = Post

class PostModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # for documentation search for django model admin
    list_display = ('title', 'created', 'updated', 'author')
    list_display_links = ('title',)
    list_filter = ('updated', 'created', 'author')
    search_fields = ('title', 'content')
    list_per_page = 15

class VisitorResource(resources.ModelResource):

    class Meta:
        model = Visitor

class VisitorModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('post', 'ip', 'created')
    list_display_links = ('post',)
    list_filter = ('post', 'created')
    search_fields = ('post__title', 'ip', 'created')
    list_per_page = 15


# Register your models here.
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Category)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Visitor, VisitorModelAdmin)
