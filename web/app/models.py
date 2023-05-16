from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self) -> str:
        return self.name