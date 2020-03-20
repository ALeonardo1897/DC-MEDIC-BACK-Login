#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#Medi_Back
from usuarios.models import User

class CustomUserAdmin(UserAdmin):

    list_display = ('email','username','first_name','last_name')
    list_filter = ('created','modified')



admin.site.register(User,CustomUserAdmin)