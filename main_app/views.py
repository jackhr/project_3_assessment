from django.shortcuts import render, redirect
from .models import Wishlist
from django.views.generic.edit import CreateView


def index(request):
  return render(request, 'index.html')