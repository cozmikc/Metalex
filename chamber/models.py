from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from backend.validators import validate_file_size



# Create your models here.

User = get_user_model()






class Chamber(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to="chamber/images", blank=True, null=True, validators=[validate_file_size])
    banner_image = models.ImageField(upload_to="chamber/images", blank=True, null=True, validators=[validate_file_size]) 
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=2, null=True, blank=True)
    file =  models.FileField(upload_to="verifiables/files", validators=[FileExtensionValidator(allowed_extensions=["pdf","doc"])], null=True,blank=True)
    is_lawfirm = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    topLawyerOfTheMonth = models.BooleanField(default=False)
    communityAccess = models.BooleanField(default=False)
    messagingAccess = models.BooleanField(default=False)
    memberRating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    online = models.BooleanField(default=False)
    free = models.BooleanField(default=True)
    lexerati = models.BooleanField(default=False)
    firm = models.BooleanField(default=False) 
    elite_firm = models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return str(self.member)


class PaymentPlan(models.Model):
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    plan = models.CharField(max_length=200, blank=True, null=True)
    paidAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.member)
        

class PracticeArea(models.Model):
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.member)  



class Qualification(models.Model):
     member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
     name = models.CharField(max_length=200, null=True, blank=True)
     degree = models.CharField(max_length=300, null=True, blank=True)
     educationInstitution = models.CharField(max_length=300, null=True, blank=True)
     educationDate = models.CharField(max_length=200, null=True, blank=True)
     membershipInstitution = models.CharField(max_length=300, null=True, blank=True)
     membershipPosition = models.CharField(max_length=200, null=True, blank=True)
     membershipDate =  models.CharField(max_length=200, null=True, blank=True)
     _id = models.AutoField(primary_key=True, editable=False)
     

  
     def __str__(self):
        return str(self.member)

     


class Contact(models.Model):
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    
    def __str__(self):
        return str(self.member)


class MemberReview(models.Model):
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


    


    










     

