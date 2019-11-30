from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length = 50, blank = False, null = True)
    weight = models.CharField(max_length = 50, blank = False, null = True)
    descrption = models.CharField(max_length = 50, blank = False, null = True)    


    def __str__(self):
        return self.name + " : " + self.descrption



class Detail(models.Model):
    login = models.CharField(max_length = 50, blank = False, null = True)
    password = models.CharField(max_length = 50, blank = False, null = True)

    def __str__(self):
        return self.login


