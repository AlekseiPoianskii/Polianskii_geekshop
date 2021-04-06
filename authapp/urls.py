from django.urls import path

from authapp.views import LoginView, RegisterView, logout, ProfileView, edit, ProfileEdit

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', ProfileEdit.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>/', RegisterView.verify, name='verify'),
]