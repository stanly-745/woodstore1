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
