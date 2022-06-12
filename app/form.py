from django.forms import ModelForm
from .models import *

# creating form

# product form

class ProductForm(ModelForm):
    class Meta:
        model=product
        fields='__all__'
        
# bill form

class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields='__all__'

# customer form
class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

# stock form
class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields='__all__'

# worker form
class WorkerForm(ModelForm):
    class Meta:
        model=Worker
        fields='__all__'