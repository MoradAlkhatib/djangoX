from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
class Car(models.Model):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    type_car = models.CharField(max_length=64)
    price = models.FloatField(max_length=32 ,null=False ,blank=False , default=0)
    model_car = models.FloatField(max_length=32)
    description = models.TextField()
    honer = models.ForeignKey( get_user_model() , on_delete = models.CASCADE ,null=False,blank=False ,default='')

    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return reverse('detail-car' , args=[str(self.pk)])
