from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_completed(self):
        return self.complete is not None

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['complete']
        db_table = 'tasks'
