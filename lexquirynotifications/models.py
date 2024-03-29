from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from chamber.models import Chamber
from questionandanswer.models import Question, Answer
from blog.models import Post
from backend.validators import validate_file_size


# Create your models here.


User = get_user_model()

class LawyerNotification(models.Model):
    user = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.text


class QuestionNotification(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)
    notificationImage =  models.ImageField(upload_to="notification/images", blank=True, null=True, validators=[validate_file_size])
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.text


class RecentQuestionNotification(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.text

class PaymentPlanNotification(models.Model):
    member = models.ForeignKey(Chamber, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return str(self.member)
