from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
  def create_user(self, username, password=None, **extra_fields):
    #if not email:
     # raise ValueErorr("Email field is required")
    if not username:
      raise ValueErorr("Username field is required")
      
    #email = self.normalize_email(email)
    user = self.model( username=username,  **extra_fields)
    user.set_password(password)
    user.save()
    return user
    
  def create_superuser(self,username, password=None, **extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_active',True)
    extra_fields.setdefault('is_superuser',True)
    
    if extra_fields.get("is_staff") is not True:
      raise ValueErorr ("Superuser must have is_staff=True.")
    
    if extra_fields.get("is_superuser") is not True:
      raise ValueErorr ( " Superuser must have is_superuser=True.")
    return self.create_user( username, password, **extra_fields) 
    


class User(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(unique=True)
  First_name = models.CharField(max_length=30,default='unknown')
  Last_name = models.CharField(max_length=30,default='user')
  birth = models.DateField(null=True)
  age = models.IntegerField(default=0)
  created_at = models.DateField(auto_now_add=True,null=True)
  #job = models.CharField()
  username = models.CharField(unique=True,max_length=100)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_medical = models.BooleanField(default=False)
  
  USERNAME_FIELD = "username"
  REQUIRED_FIELD = ['First_name','Last_name','is_medical','email','is_superuser' ]
  
  objects = UserManager()
  
  def __str__(self):
    return self.username
    
  def full_name(self):
    full_name = self.First_name+ ' ' + self.Last_name
    return full_name

