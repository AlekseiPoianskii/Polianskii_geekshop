from django.urls import path

from adminapp.views import (index, admin_users, admin_users_create, admin_users_update, admin_users_delete,
                            admin_users_rebuild, admin_products, admin_products_create, admin_products_update,
                            admin_products_delete, admin_category, admin_category_create, admin_category_update,
                            admin_category_delete)

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_users_create, name='admin_users_create'),
    path('user-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('user-delete/<int:user_id>/', admin_users_delete, name='admin_users_delete'),
    path('user-rebuild/<int:user_id>/', admin_users_rebuild, name='admin_users_rebuild'),
    path('products/', admin_products, name='admin_products'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:product_id>', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:product_id>', admin_products_delete, name='admin_products_delete'),
    path('category/', admin_category, name='admin_category'),
    path('category-create/', admin_category_create, name='admin_category_create'),
    path('category-update/<int:category_id>', admin_category_update, name='admin_category_update'),
    path('category-delete/<int:category_id>', admin_category_delete, name='admin_category_delete'),
]
