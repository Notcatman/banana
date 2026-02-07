from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False,)
    description = models.TextField(null=True, blank=True,)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

