from django.db import models
from owners.models import OwnerModel
from django.db.models.signals import pre_save
import uuid
# Create your models here.


class OwnerStoreModel(models.Model):
    CHOICES_STORE_TYPE = (
        ('gn_store', 'General Store'),
        ('ph_store', 'Pharmacy Store'),
        ('ch_store', 'Chain Shop'),
        ('sp_store', 'Sports Shop')
    )

    """
    Owner of the store
    """
    object_owner = models.ForeignKey(to=OwnerModel, on_delete=models.CASCADE, related_name='store')

    """
    Owner's store information
    """
    owner_store_id = models.UUIDField(auto_created=True, blank=True)
    owner_store_name = models.CharField(max_length=100, blank=False)
    owner_store_lcs_type = models.CharField(max_length=45, blank=False, default='N/A')
    owner_store_address = models.TextField(blank=False)
    owner_store_type = models.CharField(choices=CHOICES_STORE_TYPE, blank=False, default=CHOICES_STORE_TYPE[0][0],
                                        max_length=40)

    """
    Owner's store status
    """
    owner_store_added = models.DateTimeField(auto_now_add=True)
    owner_store_updated = models.DateTimeField(auto_now=True)
    owner_store_profile_submitted = models.BooleanField(default=False)
    owner_store_is_approved = models.BooleanField(default=False)
    owner_store_is_online = models.BooleanField(default=False)

    """
    Important methods
    """
    def __str__(self):
        return self.owner_store_name

    def is_approved(self):
        return self.owner_store_is_approved

    def is_online(self):
        return self.owner_store_is_online

    @property
    def get_owner_name(self):
        return str(self.object_owner.owner_name)

    class Meta:
        verbose_name = 'Store'


def owner_store_model_on_add_owner_store_id_auto_create(sender, instance, *args, **kwargs):
    instance.owner_store_id = uuid.uuid4().hex


pre_save.connect(owner_store_model_on_add_owner_store_id_auto_create, OwnerStoreModel)
