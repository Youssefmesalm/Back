from django.contrib import admin
from .models import User
from .forms import *
#from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
  form = UserEditForm
  add_form = UserCreationForm 
  list_display = ("id", 'full_name', 'username','email')
  list_filter = ['is_staff',]
  fieldsets = (
    (None, {'fields':('email',)}),
      ('Personal Information',{'fields':('First_name','Last_name','username','birth')}),
      ('permissions',{'fields':('is_staff','is_active','is_superuser','is_medical')})
    )
    
  add_fieldsets = (
    (None,{
      
      'classes':('wide',),
      'fields':('email','First_name','Last_name','birth','username','is_medical',"is_superuser",'password1','password2')
      ,}
    ),)
  search_fields = ('email','username',"full_name")
  filter_horizontal = ()
 
admin.site.register(User,UserAdmin)
