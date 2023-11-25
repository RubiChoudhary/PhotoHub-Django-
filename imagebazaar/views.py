from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *


def show_about_page(request):
    print("about page request")
    name = 'Rubi Choudhary'
    link = 'https://www.youtube.com/watch?v=DZrf1R9EBi8'

    data = {
        'name': name,
        'link': link
    }
    return render(request, "about.html", data)

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images,
            'cats': cats}
    return render(request, "index.html", data)

def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat= category)
    data = {'images': images,
            'cats': cats}
    return render(request, "index.html", data)

def home(request):
    return redirect('/home')