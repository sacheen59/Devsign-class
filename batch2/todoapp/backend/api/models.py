from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Task(CommonModel):
    task = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Lesson(CommonModel):
    subject = models.CharField(max_length=200)
    description = models.TextField()
