from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm


def index(request):
    return render(request, 'adminapp/index.html')


def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {'form': form,}
    return render(request, 'adminapp/admin-users-create.html', context)


def admin_users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


def admin_users_delete(request):
    pass
