from django.db import models


# Create your models here.
class table(models.Model):
    Name = models.CharField(max_length=150)
    Age = models.IntegerField

    def __str__(self):
        return self.Name


class okk(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=150)
    discription = models.TextField()

    def __str__(self):
        return self.name


class mla(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.name
