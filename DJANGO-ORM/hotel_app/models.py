from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    user_mail = models.EmailField()

    def __str__(self):
        return self.name