from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class profile_admin(admin.ModelAdmin):
    #list_display = ("gender", "date_of_birth", "address", "address")
    pass