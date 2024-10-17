from datetime import datetime

from django.utils import timezone

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from inventory.forms import ReportForm, OrderForm, ProductForm, DepartmentForm
# from django.test.client.ClientMixin import logout

from inventory.models import Order, Product, Transaction, Department, Employee
# Create your views here.
#####authentication
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard' if user.is_superuser else 'user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def admin_dashboard(request):
    # Your logic here
    orders_user = Order.objects.all()
    users = User.objects.all()[:2]
    orders_adm = Order.objects.all()[:2]
    products = Product.objects.all()[:2]
    reg_users = len(User.objects.all())
    all_prods = len(Product.objects.all())
    all_orders = len(Order.objects.all())
    transactions = Transaction.objects.all()
    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "products": products,
        "count_users": reg_users,
        "count_products": all_prods,
        "count_orders": all_orders,
        "transactions_count": transactions.count(),
        "transactions": transactions,
    }
    return render(request, 'inventory/dashboard/admin/dashboard.html', context)


# @login_required
def user_dashboard(request):
    # Your logic here
    # user_profile = UserProfile.objects.get(user=request.user)
    # orders = Order.objects.filter(created_by=request.user)
    # context = {
    #     'user_profile': user_profile,
    #     'orders': orders,
    # }
    orders_user = Order.objects.all()
    users = User.objects.all()[:2]
    orders_adm = Order.objects.all()[:2]
    products = Product.objects.all()[:2]
    reg_users = len(User.objects.all())
    all_prods = len(Product.objects.all())
    all_orders = len(Order.objects.all())
    transactions = Transaction.objects.all()
    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "products": products,
        "count_users": reg_users,
        "count_products": all_prods,
        "count_orders": all_orders,
        "transactions_count": transactions.count(),
        "transactions": transactions,
    }
    return render(request, 'inventory/dashboard/user/dashboard.html', context)


# @login_required
def orders(request):
    orders = Order.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()
    context = {"title": "Orders", "orders": orders, "form": form}
    return render(request, "inventory/orders.html", context)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReportForm
from .models import Department, Product, Transaction
from datetime import datetime

# @login_required()
def product_report(request):
    departments = Department.objects.all()
    selected_department = None
    generated_by = request.user.username  # Get the current user generating the report
    generation_date = timezone.now()
    products = []

    if request.method == "POST":
        selected_department_id = request.POST.get('department')
        if selected_department_id:
            selected_department = Department.objects.get(id=selected_department_id)
            products = Product.objects.filter(department=selected_department)
            # employee = Employee.objects.filter(employee_department=selected_department)

    context = {
        'departments': departments,
        'selected_department': selected_department,
        'products': products,
        "form": ReportForm(),
        "generated_by": generated_by,
        'generation_date' : generation_date,

    }
    return render(request, 'inventory/reports.html', context)

def products(request):
    # If the user is a superuser, display all products, otherwise filter by the current user
    if request.user.is_superuser:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(created_by=request.user)
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user  # Assign the current user as the creator
            instance.save()
            return redirect("products")
    else:
        form = ProductForm()
    
    context = {"title": "Products", "form": form, "products": products}
    return render(request, 'inventory/products.html', context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product, Department


# @login_required
def details(request, id):
    # Get the product by its id
    product = get_object_or_404(Product, id=id)

    # Get the related department based on the product's address
    department = product.department  # Assuming product.address is a ForeignKey to Department

    context_data = {
        "product": product,
        "department": department,
    }

    return render(request, "inventory/detail.html", context_data)


# @login_required()
def department(request):
    data = Department.objects.all()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department")
    else:
        form = DepartmentForm()
    return render(request, 'inventory/department.html', {"data": data, "form": form})


# @login_required
def about(request):
    return render(request, "inventory/about.html")


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

# @login_required
def ledger(request):
    products = Product.objects.all()  # Fetch all products
    context = {"products": products}  # Pass products to context
    return render(request, "inventory/ledger-book.html", context)

#
# @login_required
def orders(request):
    orders = Order.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()
    context = {"title": "Orders", "orders": orders, "form": form}
    return render(request, "inventory/orders.html", context)

# @login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect after saving
    else:
        form = ProductForm()
    return render(request, 'inventory/dashboard/admin/add_product.html', {'form': form})

# @login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect after saving
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/dashboard/admin/edit_product.html', {'form': form, 'product': product})

# @login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')  # Redirect after deleting
    return render(request, 'inventory/dashboard/admin/delete_product.html', {'product': product})

def users(request):
    users = User.objects.all()
    context = {"title": "Users", "users": users}
    return render(request, "inventory/users.html", context)

def user(request):
    context = {"profile": "User Profile"}
    return render(request, "inventory/user.html", context)


def allocate_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        from_department_id = request.POST.get('from_department_id')
        to_department_id = request.POST.get('to_department_id')
        employee = Employee.objects.get(user=request.user)  # Get the logged-in employee

        product = Product.objects.get(id=product_id)

        # Check if enough quantity is available
        if product.quantity >= quantity:
            # Create a transaction
            Transaction.objects.create(
                transact_type='ISSUE',
                item=product,
                quantity=quantity,
                user=employee,
            )
            # Update the product quantity
            product.quantity -= quantity
            product.save()
            # You can also update the quantity in the target department if needed

            return redirect('some_success_url')  # Redirect after allocation

    departments = Department.objects.all()
    products = Product.objects.all()  # Products in the employee's department

    return render(request, 'inventory/allocate_product.html', {'departments': departments, 'products': products})
