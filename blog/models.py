from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

 
class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    authorName = models.CharField(max_length=200, null=True, blank=True)
    caption = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author.name) 



class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userImage = models.ImageField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.comment + ' | ' + self.name