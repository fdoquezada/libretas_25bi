from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout  
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Usar auth_login para evitar conflictos
            return redirect('auth:dashboard')  # Redirigir al dashboard después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'autentication/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Usar auth_login para evitar conflictos
            return redirect('auth:dashboard')  # Redirigir al dashboard después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'autentication/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)  # Usar auth_logout para evitar conflictos
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'autentication/dashboard.html')
