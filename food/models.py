from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.CharField(max_length=700, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQmDtrVAUQIveJQt4rDuLsrEsJ3yyBy24LPg&usqp=CAU")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})

