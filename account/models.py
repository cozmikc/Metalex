# Create your models here.
from django.db import models

from django.contrib.auth.models import (AbstractUser, PermissionsMixin, BaseUserManager)

from backend.validators import validate_file_size


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('users must have a complete information filled')
        
        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email, name, password):
        if password is None:
            raise ValueError('password must not be empty')
        
        user = self.create_user(name=name, email=self.normalize_email(email),password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        
        user.save()

        return user
    


class UserAccount(AbstractUser,PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="images", null=True, blank=True, validators=[validate_file_size])
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_lawfirm = models.BooleanField(default=False)
    is_lawstudent = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    username = None,
    first_name = None,
    last_name = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    objects = UserAccountManager()


    def get_full_name(self):
        return self.name

    


    def __str__(self):
        return self.email









    
    
