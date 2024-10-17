from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Store, Department, Employee,
    Category, Brand, Status, Condition, Operation,
    Product, Transaction, Order, UploadedPDF
)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_address', 'time_stamp')
    search_fields = ('store_name', 'store_address')
    list_filter = ('time_stamp',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_address', 'store', 'contact')
    search_fields = ('department_name', 'department_address', 'contact')
    list_filter = ('store',)



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'employee_department')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('employee_department',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'time_stamp')
    search_fields = ('category',)
    list_filter = ('time_stamp',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand', 'time_stamp')
    search_fields = ('brand',)
    list_filter = ('time_stamp',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_code', 'time_stamp')
    search_fields = ('status_code',)
    list_filter = ('time_stamp',)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('condition',)
    search_fields = ('condition',)

class OperationAdmin(admin.ModelAdmin):
    list_display = ('operation',)
    search_fields = ('operation',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'department', 'quantity', 'brand', 'status', 'category', 'condition', 'operation')
    search_fields = ('name', 'serial')
    list_filter = ('brand', 'status', 'category')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transact_type', 'item', 'quantity', 'user', 'date')
    search_fields = ('item__name', 'user__username')
    list_filter = ('transact_type', 'date')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_by', 'order_quantity', 'date')
    search_fields = ('product__name', 'created_by__username')
    list_filter = ('date',)

class UploadedPDFAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)

# Register all models with their respective admin configurations
admin.site.register(Store, StoreAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UploadedPDF, UploadedPDFAdmin)
