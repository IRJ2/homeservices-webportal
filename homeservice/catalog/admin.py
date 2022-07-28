from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Customer

admin.site.register(Customer)
=======
from .models import Customer, Worker, review

admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(review)
>>>>>>> aa93c285801f202800f4d9ad40da8974bb3e3c4f
