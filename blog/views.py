from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def blog(request):
    queryset= Blog.objects.all()
    context= {'queryset':queryset}
    print(queryset)
    return render(request, 'blog.html',context)