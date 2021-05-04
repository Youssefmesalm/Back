from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager (BaseUserManager):
  def _create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueErorr("Email field is required")
    if not username:
      raise ValueErorr("Username field is required")
      
    email = self.normalize_email(email)
    user = self.model(email=email, username=username,  **extra_fields)
    user.set_password(password)
    user.save()
    return user
    
  def create_superuser(self, username, email, password, **extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_active',True)
    extra_fields.setdefault('is_superuser',True)
    
    if extra_fields.get("is_staff") is not True:
      raise ValueErorr ("Superuser must have is_staff=True.")
    
    if extra_fields.get("is_superuser") is not True:
      raise ValueErorr ( " Superuser must have is_superuser=True.")
    return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=255)
  username = models.CharField(unique=True,max_length=100)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  
  USERNAME_FIELD = "username"
  
  objects = CustomUserManager
  
  def __str__(self):
    return self.username