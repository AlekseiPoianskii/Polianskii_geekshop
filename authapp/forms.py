from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['username'].widget.attrs['type'] = 'email'
        self.fields['password'].widget.attrs['type'] = 'password'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
