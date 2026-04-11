from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog,Category
from assignments.models import About

def home(request):
  #categories=Category.objects.all()
  #print(categories)
  featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
  #print(featured_posts)
  posts=Blog.objects.filter(is_featured=False,status='Published')
  #print(posts)

  #fetch about us
  try:
    about=About.objects.get()
  except:
    about=None


  context={
    #'categories':categories,
    'featured_posts':featured_posts,
    'posts':posts,
    'about':about,
  }

  return render(request,'home.html',context)
  #return HttpResponse('<h1>Home page</h1>')
