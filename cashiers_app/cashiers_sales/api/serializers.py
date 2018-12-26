from owners.sales.api.serializers import SalesSerializer
from cashiers_app.cashiers_sales.models import CashierSalesModel


class CashierSaleMainSerializer(SalesSerializer):

    def get_main_owner(self):
        return self.get_request_data().user.cashier

    class Meta:
        model = CashierSalesModel
