from django.db import models


class laptop(models.Model):
    title = models.CharField(max_length=80)
    memory = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="laptop/")
    currency = models.CharField(default="USA", max_length=30)



