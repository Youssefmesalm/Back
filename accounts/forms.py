from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label='password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='password Confirmation', widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('email','username',"First_name","Last_name")
    
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
class UserEditForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()
  class Meta:
    model = User
    fields = ('email','username','First_name','Last_name', 'is_staff', 'is_superuser' ,'is_active')
    
    