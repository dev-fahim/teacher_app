from django.db import models
from owners.sales.models import SalesModel
from owners.cashiers.models import CashierModel
# Create your models here.


class CashierSalesModel(SalesModel, models.Model):
    object_owner = models.ForeignKey(CashierModel, on_delete=models.CASCADE, related_name='sales_cashier')

    @property
    def get_owner_name(self):
        return str(self.object_owner.cashier_name)

    @property
    def get_store_name(self):
        return str(self.object_owner.cashier_store)
