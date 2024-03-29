from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from backend.validators import validate_file_size




# Create your models here.

User = get_user_model()

class LawBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    coverImage = models.ImageField(upload_to="store/images", null=True, blank=True, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=["jpg", "png"])])
    file = models.FileField(upload_to="store/books", null=True,blank=True, validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc"])])
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(LawBook, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


