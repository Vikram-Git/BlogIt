from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Title',
        required=True
    )
    slug = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Slug',
        required=True
    )
    cover = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Cover Image',
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Content',
        required=True
    )
    category = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Category',
        required=True
    )
    class Meta:
        model = Post
        fields = ['title', 'slug', 'cover', 'content', 'category']