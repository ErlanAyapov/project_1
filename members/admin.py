from django.contrib import admin
from .models import Customer, UserProgress, UserPicture, UserProgress


admin.site.register(Customer)
admin.site.register(UserPicture)
admin.site.register(UserProgress)
# Register your models here.
