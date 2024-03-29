from django.db import models
from django.contrib.auth import get_user_model
from backend.validators import validate_file_size


# Create your models here.

User = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userImage = models.ImageField(upload_to="questions/images", null=True, blank=True, validators=[validate_file_size])
    name = models.CharField(max_length=200, blank=True, null=True)
    question = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    askedAt = models.DateTimeField(auto_now_add=True, null=True)
    numAnswers = models.IntegerField(null=True, blank=True, default=0)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.question


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userImage = models.ImageField(upload_to="community/images", null=True, blank=True, validators=[validate_file_size])
    name = models.CharField(max_length=200, blank=True, null=True)
    userquestion = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.TextField(null=True, blank=True)
    upVotes = models.IntegerField(null=True, blank=True, default=0)
    downVotes = models.IntegerField(null=True, blank=True, default=0)
    comments = models.IntegerField(null=True, blank=True, default=0)
    tags = models.TextField(null=True, blank=True)
    answeredAt = models.DateTimeField(auto_now_add=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
  

    def __str__(self):
        return self.answer

class Tag(models.Model):
    tag = models.CharField(max_length=200, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.tag

    


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userquestion = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(null=True, blank=True, default=0)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self): 
        return str(self.votes)

class Downvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userquestion = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(null=True, blank=True, default=0)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return str(self.votes)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userImage = models.ImageField(upload_to="community/images", null=True, blank=True, validators=[validate_file_size])
    name = models.CharField(max_length=200, blank=True, null=True)
    userquestion = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    useranswer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True, blank=True)
    commentAt = models.DateTimeField(auto_now_add=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.comment


