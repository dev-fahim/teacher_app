from django.db import models
from django.db.models.signals import post_save, pre_save
from owners.models import OwnerModel
from owners.stores.models import OwnerStoreModel
import uuid


# Create your models here.


class StoreProductModel(models.Model):

    """
    Product information
    """
    product_store = models.ForeignKey(to=OwnerStoreModel, on_delete=models.CASCADE, related_name='products')
    object_owner = models.ForeignKey(OwnerModel, on_delete=models.CASCADE, related_name='owner_product', null=True)
    product_name = models.CharField(max_length=255)
    product_id = models.UUIDField(auto_created=True)

    """
    Product prices
    """
    product_price = models.IntegerField()
    product_main_price = models.IntegerField()

    def __str__(self):
        return self.product_name

    @property
    def get_store_name(self):
        return str(self.product_store.owner_store_name)

    @property
    def get_owner_name(self):
        return str(self.object_owner.owner_name)


class ProductStatusModel(models.Model):

    """
    Product
    """
    product_origin = models.OneToOneField(StoreProductModel, on_delete=models.CASCADE, related_name='product')
    product_id = models.UUIDField()
    object_owner = models.ForeignKey(OwnerModel, on_delete=models.CASCADE, related_name='owner_product_status', null=True)

    """
    Product status
    """
    product_is_in_store = models.BooleanField(default=False)
    product_is_for_sale = models.BooleanField(default=False)
    product_quantity = models.IntegerField(default=0)

    """
    Important methods and properties
    """

    def is_is_store(self):
        return self.product_is_in_store

    def is_for_sale(self):
        return self.product_is_for_sale

    def qty_in_store(self):
        return self.product_quantity

    @property
    def get_name(self):
        return str(self.product_origin.product_name)

    @property
    def get_store(self):
        return str(self.product_origin.product_store)

    @property
    def get_price(self):
        return str(self.product_origin.product_price)

    @property
    def get_main_price(self):
        return str(self.product_origin.product_main_price)

    def __str__(self):
        return self.product_origin.product_name


def store_product_on_add_post_save_product(sender, instance, created, *args, **kwargs):
    if created:
        ProductStatusModel.objects.create(
            product_origin=instance,
            product_id=instance.product_id,
            object_owner=instance.object_owner
        )


def store_product_on_add_product_id_auto_create(sender, instance, *args, **kwargs):
    instance.product_id = uuid.uuid4().hex


post_save.connect(store_product_on_add_post_save_product, sender=StoreProductModel)
pre_save.connect(store_product_on_add_product_id_auto_create, StoreProductModel)