from django.db import models
from django.contrib.auth.models import User 


class Tweet(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(max_length=230)
    photo=models.ImageField( upload_to="photos/",blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.user.username}'



