from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Customer(models.Model):
    """Model of user module"""
    c_uid = models.EmailField(primary_key=True, max_length=20, unique=True) #User's Id
    c_password = models.CharField(max_length=20) #User's password
    c_fname = models.CharField(max_length=20) #User's first name
    c_lname = models.CharField(max_length=20,blank=True) #User's last name
    
    def __str__(self) :
        """Returns the attribute in admin page"""
        return self.c_fname 

class Worker(models.Model):
    """Model of worker module"""
    W_fname=models.CharField(max_length=200)#Worker's first name
    W_email=models.EmailField(primary_key=True,  max_length=30)#Worker's email
    W_password= models.CharField(max_length=20)#Worker's password
    W_category=models.CharField(max_length=200)##Worker's category of working 
    W_company = models.CharField(max_length=100,default='company')#Worker's company name
    W_company_motto = models.CharField(max_length=50, default='motto')#Worker's company motto
    W_desc = models.CharField(max_length=200,default='description')#Worker's description
    w_phno=models.IntegerField()#Worker's phone number
    Rate_P_Hour=models.IntegerField()#wage of worker per hour 

    def __str__(self):
        return self.W_fname

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Worker."""
        return reverse('expert_detail', args=[str(self.W_email)])

class review(models.Model):
    """Model of review module"""
    W_id=models.ForeignKey('Worker',on_delete=models.SET_NULL,null=True)#Foreign key from Worker model
    U_id=models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True)#Foreign key from Customer model
    U_review=models.TextField()#Field to write the review about the worker

    def __str__(self):
        return self.W_id
