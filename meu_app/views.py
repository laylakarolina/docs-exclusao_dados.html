from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect("home")  # Redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, "meu_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redireciona para o dashboard após login
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "meu_app/login.html", {"form": form})


@login_required
def dashboard_view(request):
    return render(request, "meu_app/dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("login")  # Redireciona para a página de login


def politica_privacidade(request):
    return render(request, 'politica_privacidade.html')


def termos_servico(request):
    return render(request, 'termos_servico.html')


def exclusao_dados(request):
    return render(request, 'meu_app/exclusao_dados.html')


# Create your views here.
