from django.shortcuts import render, redirect
from .models import Wish
from django.views.generic.edit import CreateView


def index(request):
  wishes = Wish.objects.all()
  return render(request, 'index.html', {
    'wishes': wishes,
  })

class WishCreate(CreateView):
  model = Wish
  fields = '__all__'

def delete_wish(request, wish_id):
  Wish.objects.get(id=wish_id).delete()
  return redirect('/')