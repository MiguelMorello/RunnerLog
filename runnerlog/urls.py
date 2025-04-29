from django.contrib import admin
from django.urls import path
from core import views
from accounts.views import login_view, register_view
from logs.views import adicionar_log, lista_logs, editar_log, deletar_log

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),
    path('logs/adicionar/', adicionar_log, name='adicionar_log'),
    path('logs/', lista_logs, name='lista_logs'),
    path('editar/<int:id>/', editar_log, name='editar_log'),  # URL para editar log
    path('deletar/<int:id>/', deletar_log, name='deletar_log'),  # UR
]
