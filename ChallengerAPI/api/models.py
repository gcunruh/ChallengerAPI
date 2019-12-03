from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'users'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, unique=True, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class SecurityQuestion(models.Model):
    class Meta:
        db_table = 'security_question'
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length = 250, null=False)

class Answer(models.Model):
    class Meta:
        db_table = 'answers'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    security_question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=False)

    @property
    def question(self):
        return self.security_question.question

    @property
    def username(self):
        return self.user.username
