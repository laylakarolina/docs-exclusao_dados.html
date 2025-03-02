from django.contrib import admin
# Importa "include" para incluir URLs de apps
from django.urls import path, include
from meu_app import views

urlpatterns = [
    path("admin/", admin.site.urls),  # Painel de administração do Django
    path("", include("meu_app.urls")),  # Inclui todas as URLs do "meu_app"
    path('politica-privacidade/', views.politica_privacidade,
         name='politica_privacidade'),
]
