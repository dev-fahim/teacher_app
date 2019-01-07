from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserLevelModel(models.Model):
    LEVEL_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_level')
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return self.user.username
