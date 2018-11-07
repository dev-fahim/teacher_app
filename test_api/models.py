from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class TestApiModel(models.Model):

    post_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post_heading = models.CharField(max_length=44, blank=False)
    post_title = models.CharField(max_length=44, blank=True)
    post_body = models.TextField()
    post_added = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_heading

    class Meta:
        verbose_name = "Test Post API"
