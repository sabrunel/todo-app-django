from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many-to-one relationship between users and list items
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta: # add metadata to the model
        ordering = ['is_completed', '-is_important']