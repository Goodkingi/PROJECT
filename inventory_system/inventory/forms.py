# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms


from .models import Product, Brand, Status, Category, Condition, Operation, Department

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'serial',
            'batch',
            'description',
            'quantity',
            'brand',
            'status',
            'department',
            'category',
            'condition',
            'operation',
        ]

    def clean_serial(self):
        serial = self.cleaned_data.get('serial')
        if Product.objects.filter(serial=serial).exists():
            raise forms.ValidationError("Serial number must be unique.")
        return serial



from django import forms
from django.forms import ModelForm, Form
from .models import Product, Department, Employee, Status
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventory.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]


from django import forms
from .models import Department

class ReportForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=True)

# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
