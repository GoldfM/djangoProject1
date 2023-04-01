from django.shortcuts import render, HttpResponse, redirect
from advertisement.models import Advertisment
from advertisement.forms import AddItemForm

base_context =  {'title': 'ZEO', 'home_page_url': '/'}
def base(requests):
    return render(requests, 'home.html',base_context)

def list_item(requests, number):
    return HttpResponse(f'<h1>Number {number}</h1>')

def board(requests):
    posts = Advertisment.objects.all()
    return render(requests, 'board/board.html',{'title':'ZEO','posts': posts,'home_page_url': '/'})

def item(requests, name):
    post = Advertisment.objects.get(slug=name)
    return render(requests, 'item.html',{'title':'ZEO','post': post,'home_page_url': '/'})

def add_item(requests):
    if requests.method == 'POST':
        form = AddItemForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddItemForm()
    return render(requests, 'adder.html', {'form': form})