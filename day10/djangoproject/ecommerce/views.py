from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from verify_email.email_handler import ActivationMailManager
from . import models
from .models import Customer
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save(commit=False)

            inactive_user = ActivationMailManager.send_verification_link(
                request, form)
            # inactive_user.cleaned_data['email']

    context = {'form': form}
    return render(request, "ecommerce/signup.html", context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get("fullname")
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        password = request.POST.get('password')
        if Customer.objects.filter(username=username).first():
            return redirect('/register')
        if Customer.objects.filter(email=email).first():
            return redirect('/register')
        auth_token = str(uuid.uuid4())
        user_obj = Customer(username=username, email=email, fullname=fullname, gender=gender,
                            phone_number=phone_number, date_of_birth=date_of_birth, auth_token=auth_token, password=password)

        user_obj.save()
        send_mail_after_registration(email, auth_token)
        return redirect('/token')

    return render(request, 'ecommerce/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            Customer.objects.get(email=email, password=password)
            return redirect('/logout')
        except Exception as e:
            print(e)

    return render(request, 'ecommerce/login.html')


def token_sent(request):
    return render(request, 'ecommerce/token.html')


def success(request):
    return render(request, 'ecommerce/success.html')


def logout(request):
    return render(request, 'ecommerce/logout.html')


def verify(request, auth_token):
    user_obj = Customer.objects.filter(auth_token=auth_token).first()
    if user_obj:
        user_obj.is_verified = True
        user_obj.save()
        return redirect('/success')


def send_mail_after_registration(email, token):
    subject = "Your account needs to be verified"
    message = f"verify mail http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
