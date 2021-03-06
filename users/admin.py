from django.contrib import admin

# Register your models here.
# users/admin.py

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]  #show what fields are displayed

admin.site.register(CustomUser, CustomUserAdmin)