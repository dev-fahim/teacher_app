from django.contrib import admin
from cashiers.models import CashierModel, CashierSalesPermissionsModel
# Register your models here.

admin.site.register(CashierModel)
admin.site.register(CashierSalesPermissionsModel)
