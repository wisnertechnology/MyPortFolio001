from django.db import models

# Create your models here.
# portfolio/models.py
from django.db import models

class Comment(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Comment from {self.full_name}"
