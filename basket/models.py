from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """ модель заказа """
    last_name = models.CharField(max_length=100, verbose_name='Фамілія')
    first_name = models.CharField(max_length=100, verbose_name='Ім\'я')
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    order = models.CharField(max_length=500)
    price = models.IntegerField()
    payment = models.BooleanField(default=False)
    user_id = models.CharField(max_length=10)

    def __str__(self):
        return self.order


