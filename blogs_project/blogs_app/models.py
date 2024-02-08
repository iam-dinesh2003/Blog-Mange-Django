from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you want to delete the Blog when the associated User is deleted

    def __str__(self):
        return self.title
