from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import Product, ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminForm, CategoryAdminForm


@user_passes_test(lambda u: u.is_staff, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_users_update(request, user_id=None):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form,
               'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_users_delete(request, user_id=None):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_users_rebuild(request, user_id=None):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_products_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminForm(instance=product)
    context = {'form': form,
               'product': product}
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_products_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_products'))


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_category(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
    else:
        form = CategoryAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_category_update(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, files=request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
    else:
        form = CategoryAdminForm(instance=category)
    context = {'form': form,
               'category': category}
    return render(request, 'adminapp/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='/')
def admin_category_delete(rerquest, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_category'))
