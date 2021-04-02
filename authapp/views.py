from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from basketapp.models import Basket


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f'Для активации учетной записи {user.username} перейдите по ссылке'

    message = f'для подтверждения учетной записи {user.username} пройдите по ссылке: \n{settings.DAMINE_NAME}' \
              f'{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email, ], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expires():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        print(f'Error activation user: {user}')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'Error activation user: {e.args}')
        return HttpResponseRedirect(reverse('mainapp:index'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form,
               'title': 'GeekShop - Авторизация'}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form,
               'title': 'GeekShop - Регистрация'}
    return render(request, 'authapp/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
