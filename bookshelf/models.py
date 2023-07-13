from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title=models.TextField()
    description=models.TextField(null=True)
    pdf=models.FileField(upload_to='books/pdf',null=True, blank=True)
    authors=models.ManyToManyField(User)

    def __str__(self):
        return self.title