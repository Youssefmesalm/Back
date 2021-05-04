import jwt
from django.conf import settings
from datetime import datetime
from rest_framework.authentication import BaseAuthentication
from accounts.models import CustomUser

class Authentication(BaseAuthentication):
  def authenticate(self, request):