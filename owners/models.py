from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()


class OwnerModel(models.Model):

    """
    Personal information
    """
    owner_name = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='owner')
    owner_birth_date = models.DateField(blank=True, null=True)
    owner_ps_address = models.TextField(blank=False, default='N/A')
    owner_pm_address = models.TextField(blank=False, default='N/A')

    """
    Owner's status
    """
    owner_joined = models.DateTimeField(auto_now_add=True)
    owner_info_updated = models.DateTimeField(auto_now=True)
    owner_is_active = models.BooleanField(default=False)
    owner_profile_submitted = models.BooleanField(default=False)
    owner_is_approved = models.BooleanField(default=False)
    owner_is_online = models.BooleanField(default=False)

    """
    Important methods
    """
    def __str__(self):
        return self.owner_name.username

    def is_active(self):
        return self.owner_is_active

    def is_approved(self):
        return self.owner_is_approved

    def is_online(self):
        return self.owner_is_online

    class Meta:
        verbose_name = 'Owner'


"""All signals"""

"""
def user_register_post_save_owner(sender, instance, created, *args, **kwargs):
    if created:
        OwnerModel.objects.create(owner_name=instance)


post_save.connect(user_register_post_save_owner, sender=User)
"""

"""-------------------"""
