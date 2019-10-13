# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location

# Create your views here.


def image_display(request):
    locations = Location.objects.all()
    if request.GET.get('location'):
        image = Image.filter_by_location(request.GET.get('location'))
    elif request.GET.get('search_term'):
        image = Image.search_results(request.GET.get('search_term'))
    else:
        image = Image.objects.all()
    return render(request, 'all-image/today-image.html', {"locations":locations,"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'all-image/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-image/search.html',{"message":message})

def image(request,image_id):
    try:
        images = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-image/image.html", {"image":images})