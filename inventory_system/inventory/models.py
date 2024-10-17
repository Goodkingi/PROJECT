from django.db import models
from django.contrib.auth.models import User
from django.db import models
import uuid
from django.contrib.auth.models import User

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name} - {self.store_address}"


class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    department_address = models.CharField(max_length=100)
    block = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.department_name}, {self.department_address}, {self.store}, {self.contact}, {self.block.title()}"


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.staff_first_name} {self.staff_last_name} - {self.username}"


class Category(models.Model):
    CATEGORY_TYPE = (
        # Electronics Categories
        ('ELECTRONIC', 'Electronic'),
        ('COMPUTER', 'Computer'),
        ('PRINTER', 'Printer'),
        ('SCANNER', 'Scanner'),
        ('MONITOR', 'Monitor'),
        ('MOUSE', 'Mouse'),
        ('KEYBOARD', 'Keyboard'),
        ('HEADPHONES', 'Headphones'),
        
        # Office Supplies Categories
        ('PAPER', 'Paper'),
        ('STATIONERY', 'Stationery'),
        ('PEN', 'Pen'),
        ('FOLDER', 'Folder'),
        ('NOTEBOOK', 'Notebook'),
        ('MARKER', 'Marker'),

        # Office Furniture Categories
        ('TABLE', 'Table'),
        ('CHAIR', 'Chair'),
        ('CABINET', 'Cabinet'),
        ('SHELF', 'Shelf'),
        ('DESK', 'Desk'),
        ('SOFA', 'Sofa'),

        # Miscellaneous
        ('OFFICE', 'Office'),
        ('OTHER', 'Other'),
    )
    
    category = models.CharField(max_length=255, choices=CATEGORY_TYPE, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Brand(models.Model):
    BRAND_TYPE = (
        # Electronics Brands
        ('LENOVO', 'Lenovo'),
        ('HP', 'HP'),
        ('DELL', 'Dell'),
        ('APPLE', 'Apple'),
        ('ASUS', 'Asus'),
        ('ACER', 'Acer'),
        ('SAMSUNG', 'Samsung'),
        ('MICROSOFT', 'Microsoft'),
        ('TOSHIBA', 'Toshiba'),
        ('SONY', 'Sony'),
        ('LG', 'LG'),
        ('PANASONIC', 'Panasonic'),
        ('CANON', 'Canon'),

        # Office Furniture Brands
        ('STEELCASE', 'Steelcase'),
        ('HERMAN_MILLER', 'Herman Miller'),
        ('HAWORTH', 'Haworth'),
        ('HON', 'HON'),
        ('ALLSTEEL', 'Allsteel'),
        ('KNOLL', 'Knoll'),
        ('AERON', 'Aeron'),
        ('XCHAIR', 'XChair'),
        ('FLEXISPOT', 'FlexiSpot'),
        ('ERGOTECH', 'Ergotech'),

        # Office Supplies & Stationery Brands
        ('STABILO', 'Stabilo'),
        ('PAPER_MATE', 'Paper Mate'),
        ('BIC', 'BIC'),
        ('3M', '3M'),
        ('PENTEL', 'Pentel'),
        ('FABER_CASTELL', 'Faber-Castell'),
        ('DYMO', 'Dymo'),
        ('POST_IT', 'Post-it'),
        ('QUILL', 'Quill'),
        ('EXPO', 'Expo'),
        ('PARKER', 'Parker'),

        # Cabinet/Storage Brands
        ('HUSKY', 'Husky'),
        ('HON_STORAGE', 'HON Storage'),
        ('SAFCO', 'Safco'),
        ('GLADIATOR', 'Gladiator'),
    )
    
    brand = models.CharField(max_length=255, choices=BRAND_TYPE, null=True)

    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand


class Status(models.Model):
    STATUS_OPERATION = (
        ('AVAILABLE', 'Available'),
        ('NOT AVAILABLE', 'Not Available'),
    )
    status_code = models.CharField(max_length=50, choices=STATUS_OPERATION, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_code


class Condition(models.Model):
    CONDITION_TYPE = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE, null=True)

    def __str__(self):
        return self.condition


class Operation(models.Model):
    OPERATION_TYPE = (
        ('WORKING', 'Working'),
        ('NOT WORKING', 'Not Working'),
    )
    operation = models.CharField(max_length=100, choices=OPERATION_TYPE, null=True)

    def __str__(self):
        return self.operation


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    serial = models.CharField(max_length=100, null=True, unique=True)
    batch = models.CharField(max_length=50, null=True, default="TSF/0000-0000")
    description = models.TextField(max_length=200, null=True)
    quantity = models.IntegerField(default=0)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, null=True)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_stamp = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.serial}) - Qty: {self.quantity}"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('RECEIVE', 'Receive'),
        ('ISSUE', 'Issue'),
    )
    transact_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)  # Link to Employee
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.transact_type} - {self.item.name} - {self.date}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} ordered quantity {self.order_quantity}"


class UploadedPDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded at {self.uploaded_at}"
