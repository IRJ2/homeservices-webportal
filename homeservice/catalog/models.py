from django.db import models

class Customer(models.Model):
    """Model of user module"""
    c_uid = models.CharField(max_length=20) #User's Id
    c_password = models.CharField(max_length=20) #User's password
    c_fname = models.CharField(max_length=20) #User's first name
    c_lname = models.CharField(max_length=20) #User's last name
    
    def __str__(self) :
        """Returns the attribute in admin page"""
        return self.c_fname 