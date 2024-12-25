from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name= "Марка мащаины")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= "Владелец")
    entry_time = models.DateTimeField(verbose_name= "Дата и время въезда")
    parking_fee = models.DecimalField(max_digits=6, decimal_places=2, verbose_name= "Стоимость стоянки")
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name= "Размер скиидки")
    debt = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Задолженность" )

    def __str__(self):
        return f"{self.brand} - {self.owner.username}"

