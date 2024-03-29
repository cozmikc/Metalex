from django.db import models
from backend.validators import validate_file_size
from django.core.validators import FileExtensionValidator


# # Create your models here.



class Category(models.Model):
    categoryLetter = models.CharField(max_length=100, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.categoryLetter   

class CategoryName(models.Model):
    userCategory =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="categories/images", null=True, blank=True, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=["jpg", "png"])])
    name = models.CharField(max_length=100, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

    