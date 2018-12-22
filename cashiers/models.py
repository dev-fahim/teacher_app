from django.db import models
from stores.models import OwnerStoreModel
from owners.models import OwnerModel
from django.contrib.auth.models import User
import uuid
# Create your models here.


class CashierModel(models.Model):
    cashier_name = models.CharField(max_length=50)
    cashier_id = models.UUIDField(auto_created=True, default=uuid.uuid4().hex)

    cashier_store = models.OneToOneField(OwnerStoreModel, on_delete=models.CASCADE, related_name='cashier_store')
    object_owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cashier_model')
