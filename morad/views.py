from django.shortcuts import render
from morad.models import Car
from django.views.generic import (ListView,DetailView,DeleteView,UpdateView,CreateView)
from django.urls.base import reverse_lazy
class ListCars(ListView):
    template_name = 'cars/cars.html'
    model = Car

class DetailCar(DetailView):
    template_name = 'cars/details.html'
    model = Car

class CreateCar(CreateView):
    template_name = 'cars/create.html'
    model = Car
    fields = ['name','color','type_car','model_car','description','honer']


class UpdateCar(UpdateView):
    template_name = 'cars/update.html'
    model = Car
    fields = ['name','color','type_car','model_car','description','honer']

class DeleteCar(DeleteView):
    template_name = 'cars/delete.html'
    model = Car
    success_url = reverse_lazy("list-cars")
