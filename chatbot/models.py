from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatHistory(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.prompt
