from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import State, District, Hospital

# Register your models here.

# admin.site.unregister(User)


# @admin.register(newUser)
# class NewUserAdmin(UserAdmin):
#     pass

admin.site.register(State)
admin.site.register(District)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'district', 'contact']
