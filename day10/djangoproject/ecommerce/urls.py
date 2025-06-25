from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('token/', views.token_sent, name="token_sent"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('success/', views.success, name='sucecss'),
    path('logout/', views.logout, name="logout"),
]
