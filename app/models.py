from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
