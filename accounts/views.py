from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Validate input
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('user_list')  # Replace 'home' with your desired redirect
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password1
        )
        user.save()
        print("User registered successfully.")
        return redirect('login')  # Change to your desired redirect URL
    else:
        return render(request, 'register.html')
def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')  # Redirect to login page or anywhere else
# @login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
# @login_required
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('user_list')

    return render(request, 'edit_user.html', {'user': user})
# @login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_list')

    return render(request, 'delete_user.html', {'user': user})
