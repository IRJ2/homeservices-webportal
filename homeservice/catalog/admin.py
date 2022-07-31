from django.contrib import admin

# Register your models here.

from .models import Customer, Worker, review

admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(review)

