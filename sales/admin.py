from django.contrib import admin
from sales.models import SalesModel, DailySalesModel
# Register your models here.


admin.site.register(SalesModel)
admin.site.register(DailySalesModel)
