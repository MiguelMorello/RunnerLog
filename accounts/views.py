from django.contrib.auth import authenticate, login,  get_user_model
from django.shortcuts import render, redirect
# from .models import CustomUser
# from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('/logs')  # redireciona pra home
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email já cadastrado.'})
        user = User.objects.create_user(email=email, name=name, password=password)
        login(request, user)  # já loga automaticamente após cadastro
        return redirect('/logs')
    return render(request, 'register.html')