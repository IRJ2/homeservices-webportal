from django.db import models

<<<<<<< HEAD
# Create your models here.
class worker(models.Model):

    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200,blank=True)
    W_Id=models.IntegerField(primary_key=True)
    E_Mail=models.EmailField(max_length=300,blank=True,null=True)
    W_Category=models.CharField(max_length=200)
    W_Pin=models.IntegerField()
    w_Phno=models.IntegerField()
    Rate_P_Hour=models.IntegerField()

    def __str__(self):
        return self.W_Id

class review(models.Model):

    W_Id=models.ForeignKey('worker',on_delete=models.SET_NULL,null=True)
    U_id=models.ForeignKey('user',on_delete=models.SET_NULL,null=True)
    U_review=models.TextField()

    def __str__(self):
        return self.W_Id


    


=======
class Customer(models.Model):
    """Model of user module"""
    c_uid = models.CharField(max_length=20) #User's Id
    c_password = models.CharField(max_length=20) #User's password
    c_fname = models.CharField(max_length=20) #User's first name
    c_lname = models.CharField(max_length=20) #User's last name
    
    def __str__(self) :
        """Returns the attribute in admin page"""
        return self.c_fname 
>>>>>>> 7d2c849801bd9da31ca7acc8d859cb9dc9e004f9
