from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login_view"),
    path("verify/", views.verify, name="verify"),
    path("profile/", views.profile, name="profile"),
    path("logout/",views.logout_view,name="logout_view"),
    path('password/', views.change_password, name='change_password'),
]
