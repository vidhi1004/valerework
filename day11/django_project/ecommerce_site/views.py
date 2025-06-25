from django.shortcuts import render, redirect
from .forms import UserSignUp
import uuid
from .models import Customer
from django.core.mail import EmailMessage
from django.conf import settings
import random
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def index(request):
    return render(request,"ecommerce_site/index.html")

def signup(request):
    form = UserSignUp()
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        name = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dob = request.POST["date_of_birth"]
        gender = request.POST["gender"]
        phone = request.POST["phone_number"]
        email = request.POST["email"]
        password = request.POST["password1"]

        if Customer.objects.filter(username=name).exists():
            messages.success(request, "username exists")
            return redirect('/signup')
        if Customer.objects.filter(email=email).exists():
            messages.success(request, "email already in use")
            return redirect('/signup')

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            otp = generateOTP()
            request.session['pending_user'] = {
                "username": name,
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": dob,
                "gender": gender,
                "phone_number": phone,
                "email": email,
                "password1": password,
                "is_active": False
            }
            request.session['otp'] = otp

            context = {
                'user': name,
                'otp': otp,
            }

            message = render_to_string('email/email_activation.html', context)

            email = EmailMessage(
                subject="Your account needs to be verified",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )

            email.content_subtype = 'html'

            email.send()

            return redirect('/verify')

    context = {'form': form}
    return render(request, 'ecommerce_site/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = Customer.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, "username incorrect")
            return redirect('/login')
        if not user_obj.is_active:
            messages.success(request, "please verify the email first.")
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, "Incorrect Password")
            return redirect('/login')
        login(request, user)
        return redirect('/home')

    return render(request, "ecommerce_site/login.html")


def verify(request):
    if request.method == "POST":
        user_input_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        user_data = request.session.get('pending_user')

        if int(user_input_otp) == int(session_otp) and user_data:
            Customer.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password1'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                date_of_birth=user_data["date_of_birth"],
                gender=user_data["gender"],
                phone_number=user_data["phone_number"],
                is_active=True,
            )
            request.session.pop("pending_user", None)
            request.session.pop("otp", None)
            return redirect("login_view")
        else:
            messages.success(request, "wrong otp")
    return render(request, "ecommerce_site/verify.html")

@login_required
def home(request):
    return render(request, "ecommerce_site/home.html")


def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required
def profile(request):
    data = Customer.objects.all().filter(username=request.user)
    print(data)
    context = {
        'data': data,
        'current_user': request.user,
    }
    return render(request, 'ecommerce_site/profile.html', context)


def generateOTP():
    otp = random.randint(100000, 999999)
    return otp

@login_required
def change_password(request):
    if request.method =='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            logout_view(request)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ecommerce_site/change_password.html', {
        'form': form
    })