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
