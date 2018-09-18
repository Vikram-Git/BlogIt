from django.contrib import admin
from django.urls import re_path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^posts/', include('posts.urls', namespace='posts')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)