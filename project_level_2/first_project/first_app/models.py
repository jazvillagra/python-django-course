from django.db import models

# Create your models here.

class Users(models.Model):
    first_name= models.CharField(max_length=264, blank=False)
    last_name= models.CharField(max_length=264, blank=False)
    email= models.EmailField(unique=True)
    def __str__(self):
        return self.first_name
    
    