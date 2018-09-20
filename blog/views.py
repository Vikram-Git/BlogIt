from django.shortcuts import render, redirect

def base(request):
    return render(request, 'base.html')

def post_redirect(request):
    return redirect('posts:post_list')