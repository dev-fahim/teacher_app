from django.db import models
from owners.stores.models import OwnerStoreModel
from owners.models import OwnerModel
from django.contrib.auth.models import User
import uuid
# Create your models here.


class CashierModel(models.Model):
    cashier_name = models.CharField(max_length=50)
    cashier_id = models.UUIDField(auto_created=True)

    cashier_store = models.OneToOneField(OwnerStoreModel, on_delete=models.CASCADE, related_name='cashier_store')
    cashier_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cashier')
    object_owner = models.ForeignKey(OwnerModel, on_delete=models.CASCADE, related_name='cashier_owner')

    def __str__(self):
        return self.cashier_name


def cashier_model_cashier_id_auto_create(sender, instance, *args, **kwargs):
    instance.cashier_id = uuid.uuid4().hex


models.signals.pre_save.connect(cashier_model_cashier_id_auto_create, CashierModel)
