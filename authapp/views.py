from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from authapp.models import User, UserProfile
from basketapp.models import Basket


# Log in User
class LoginView(FormView):
    model = User
    success_url = reverse_lazy('index')
    form_class = UserLoginForm
    template_name = 'authapp/login.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(
                username=usr,
                password=pwd,
            )

            if user and user.is_active:
                login(request, user)
                return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Login'
        return context


# Register User
class RegisterView(FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_mail(user):
                messages.success(request,
                                 'Вы успешно зарегистрировались! Ссылка с активацией профиля отправлена на почту.')
                return redirect(self.success_url)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def send_verify_mail(self, user):
        verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

        title = f'Для активации учетной записи {user.username} перейдите по ссылке'

        message = f'для подтверждения учетной записи {user.username} пройдите по ссылке: \n{settings.DOMAIN_NAME}' \
                  f'{verify_link}'
        return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email, ], fail_silently=False)

    def verify(request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expires():
                user.is_active = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, 'authapp/verification.html')
            print(f'Error activation user: {user}')
            return render(request, 'authapp/verification.html')
        except Exception as e:
            print(f'Error activation user: {e.args}')
            return HttpResponseRedirect(reverse('mainapp:index'))

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Registration'
        return context


# Profile info
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    form_class_second = UserProfileEditForm
    template_name = 'authapp/profile.html'

    def get_success_url(self):
        return reverse('auth:profile', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Profile'
        self_pk = self.object.pk
        user = User.objects.get(pk=self_pk)
        context['baskets'] = Basket.objects.filter(user=user)
        context['profile_form'] = self.form_class_second(instance=user.userprofile)
        return context


# Log out User
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
