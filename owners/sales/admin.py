from django.contrib import admin
from owners.sales.models import SalesModel, DailySalesModel
# Register your models here.


admin.site.register(SalesModel)
admin.site.register(DailySalesModel)
