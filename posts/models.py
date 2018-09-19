from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Author(models.Model):
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    link = models.URLField(max_length=300)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.user.username


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:category_list', kwargs={'category_title': self.title})

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(TimeStamp):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    cover = models.ImageField(upload_to='images/covers')
    cover_thumb = ImageSpecField(source='cover',
                                 processors=[ResizeToFill(400, 250)],
                                 format='JPEG',
                                 options={'quality':80})
    content = RichTextUploadingField()
    category = models.ManyToManyField('Category')
    meta_keywords = models.CharField(max_length=120,
                                     help_text='Keywords should be separated by commas.')
    meta_description = models.TextField(max_length=300, null=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'post_slug': self.slug})

    @property
    def total_visitors(self):
        all_visitors = Visitor.objects.filter(post__pk=self.pk)
        return all_visitors.count()
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']


def get_unique_slug(self):
    slug = slugify(self.title)
    new_slug = slug
    num = 1
    while Post.objects.filter(slug=new_slug).exists():
        new_slug = '{}-{}'.format(slug, num)
        num += 1
    return new_slug

def post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance)

pre_save.connect(post_reciever, sender=Post)


class Visitor(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=40)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'
