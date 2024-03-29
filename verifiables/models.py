from django.db import models
from django.core.validators import FileExtensionValidator
from chamber.models import Chamber

# Create your models here.




class Verifiable(models.Model):
    chamberMember = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    file =  models.FileField(upload_to="verifiables/files", validators=[FileExtensionValidator(allowed_extensions=["pdf","doc"])], null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    uploadedAt = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return str(self.chamberMember)


    
 
