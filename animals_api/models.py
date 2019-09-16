from django.contrib.auth.models import User
from django.db import models


class Animals(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    birthday_date = models.DateField(null=True, blank=True)


class Cat(Animals):
    class Meta:
        db_table = "cats"
        verbose_name = "Cat"
        verbose_name_plural = "Cats"
        ordering = ["-id"]


class Dog(Animals):
    class Meta:
        db_table = "dogs"
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"
        ordering = ["-id"]
