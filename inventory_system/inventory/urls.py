from . import views
from django.urls import path

urlpatterns = [
    
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/user/', views.user_dashboard, name='user_dashboard'),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    # path('dashboard/admin/ledger/', views.ledger_view, name='admin_ledger_view'),  # Updated path
    path("orders/", views.orders, name="orders"),
    path("products/", views.products, name="products"),
    path('reports/', views.product_report, name='reports'),
    path('about/', views.about, name="about"),
    path('ledger/', views.ledger, name="ledger"),
    path('department/', views.department, name="department"),
    path("details/<int:id>", views.details, name="detail-page"),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
     path('allocate/',views.allocate_product,name='allocate_product'),
]
