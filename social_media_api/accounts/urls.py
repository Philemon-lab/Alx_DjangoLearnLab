from django.urls import path
from . import views
from .views import unfollow_user

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),

]