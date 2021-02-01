from django.db import models

# Create your models here.

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    def __str__(self):
        return self.first_name
    

