from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, termos_servico, exclusao_dados

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("termos-servico/", termos_servico, name="termos_servico"),
    path("exclusao-dados/", exclusao_dados, name="exclusao_dados"),
]
