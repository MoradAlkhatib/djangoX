from django.db.models.expressions import F
from django.urls import path
from .views import *
urlpatterns =[
    path('',ListCars.as_view() , name = 'list-cars' ),
    path('<int:pk>',DetailCar.as_view() , name='detail-car' ),
    path('create',CreateCar.as_view() , name='create-car' ),
    path('<int:pk>/update',UpdateCar.as_view() , name='update-car' ),
    path('<int:pk>/delete',DeleteCar.as_view() , name='delete-car' ),
    
    ]