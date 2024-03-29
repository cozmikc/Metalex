from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from backend.validators import validate_file_size
from lawbooks.models import LawBook
from chamber.models import Chamber

# Create your models here.

User = get_user_model()




class BookmarkedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(LawBook, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    coverImage = models.ImageField(upload_to="store/images", null=True, blank=True, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=["jpg", "png"])])
    category = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)


class BookmarkedLawyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to="chamber/images", blank=True, null=True, validators=[validate_file_size])
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return str(self.user)