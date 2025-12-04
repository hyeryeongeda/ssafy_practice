from django.db import models

# Create your models here.

# AbstractUser : 자동으로 필드를 제공(로그인, 권한 관리 등)
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass