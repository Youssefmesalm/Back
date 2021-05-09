from django.contrib import admin
from .models import User
#from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Register your models here.
class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label='password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='password Confirmation', widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('email','username',)
    
  def save(self, commit=True):
    user= super().save(commit=False)
    password1=self.cleaned_data.get("password1")
    password2=self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2 :
      raise ValidationError("Passwords don't match")
    else:
      user.set_password(self.cleaned_data["password1"])
      
    if commit:
      user.save()
    return user
class UserChanegeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()
  class Meta:
    model = User
    fields = ('email','username', 'is_staff', 'is_superuser' ,'is_active')
    
    
class UserAdmin(BaseUserAdmin):
  form = UserChanegeForm
  add_form = UserCreationForm 
  list_display = ( 'full_name', 'username','email')
  list_filter = ['is_staff',]
  fieldsets = (
    (None, {'fields':('email',)}),
      ('Personal Information',{'fields':('First_name','Last_name','username','birth')}),
      ('permissions',{'fields':('is_staff','is_active','is_superuser','is_medical')})
    )
    
  add_fieldsets = (
    (None,{
      
      'classes':('wide',),
      'fields':('email','First_name','Last_name','birth','username','is_medical','password1','password2')
      ,}
    ),)
  search_fields = ('email','username')
  filter_horizontal = ()
 
admin.site.register(User,UserAdmin)
