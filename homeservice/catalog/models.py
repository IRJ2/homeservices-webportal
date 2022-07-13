from django.db import models

class Customer(models.Model):
    c_uid = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)
    c_fname = models.CharField(max_length=20)
    c_lname = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.c_fname