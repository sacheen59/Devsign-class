from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parents', 'Parents')
    )
    role = models.CharField(max_length=30,choices=ROLE_CHOICES, default='student')
    otp = models.CharField(max_length=6,blank=True, null=True)
    otp_created = models.DateTimeField(null=True, blank=True)

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Task(CommonModel):
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.task


class Lesson(CommonModel):
    subject = models.CharField(max_length=200)
    description = models.TextField()
