from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib import messages

from .models import ShowManager

# Create your views here.
def index(request):
    context={
        "shows": models.Show.objects.all()
    }
    return render(request,'shows.html',context)

def new(request):
    return render(request,'index.html')

def add_show(request):
    if request.method == "POST":
        models.Show.objects.create(title=request.POST["title"],network=request.POST["network"],release_date=request.POST["release_date"],description = request.POST["description"])
        return redirect('/shows/'+str(models.Show.objects.last().id))

def show_detail(request,show_id):
    context={
        'show': models.Show.objects.get(id=show_id)
    }
    return render(request,'show.html',context)

def edit(request,show_id):
    now = models.Show.objects.get(id=show_id).release_date
    date = now.strftime("%Y-%m-%d")
    context={
        'show':models.Show.objects.get(id=show_id),
        'date':date
    }
    return render(request,'edit.html',context)
    
def update(request,show_id):
    update_show = models.Show.objects.get(id=show_id)
    update_show.title = request.POST["title"]
    update_show.network = request.POST["network"]
    update_show.release_date = request.POST["release_date"]
    update_show.description = request.POST["description"]
    update_show.save()
    return redirect('/shows/'+str(show_id))

def delete(request,show_id):
    delete_show = models.Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/')
