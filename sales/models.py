from django.db import models
from owners.models import OwnerModel
from stores.models import OwnerStoreModel
from products.models import StoreProductModel
from django.db.models.signals import pre_save
import uuid
# Create your models here.


class SalesModel(models.Model):

    object_owner = models.ForeignKey(OwnerModel, on_delete=models.DO_NOTHING, related_name='sales_owner')
    store = models.ForeignKey(OwnerStoreModel, on_delete=models.DO_NOTHING, related_name='sales_store')

    sale_id = models.UUIDField()
    total_discounted = models.IntegerField()

    @property
    def get_owner_name(self):
        return str(self.object_owner.owner_name)

    @property
    def get_store_name(self):
        return str(self.store.owner_store_name)


def sales_model_sale_id_pre_save(sender, instance, *args, **kwargs):
    instance.sale_id = uuid.uuid4().hex


pre_save.connect(sales_model_sale_id_pre_save, SalesModel)


class DailySalesModel(models.Model):

    sales = models.ForeignKey(SalesModel, on_delete=models.CASCADE, related_name='sales_object')
    product = models.ForeignKey(StoreProductModel, on_delete=models.CASCADE, related_name='sales_product')
    discounted = models.IntegerField()

    @property
    def get_product_name(self):
        return str(self.product.product_name)
