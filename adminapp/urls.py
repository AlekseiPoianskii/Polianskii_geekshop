from django.urls import path

from adminapp.views import (index, UserListView, UserCreateView, UserUpdateView, UserDeleteView,
                            ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                            CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView)

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category-create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category-delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_category_delete'),
]
