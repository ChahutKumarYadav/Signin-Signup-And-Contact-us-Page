from django.db import models


# Create your models here.
class CarInfo(models.Model):
    brand_name = models.CharField(max_length=100)
    modle_name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.brand_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name