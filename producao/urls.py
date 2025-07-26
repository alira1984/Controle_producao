from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaquinaViewSet, TurnoViewSet, ProducaoDiariaViewSet, cadastro_producao, home, listar_producao
from . import views
from django.urls import path
from .views import home, listar_producao, cadastro_producao


router = DefaultRouter()
router.register(r'maquinas', MaquinaViewSet)
router.register(r'turnos', TurnoViewSet)
router.register(r'producao', ProducaoDiariaViewSet)



urlpatterns = [
    path('', home, name='home'),                          # Página inicial com formulário
    path('listagem/', listar_producao, name='listagem'),  # Página de visualização
    path('cadastro/', cadastro_producao, name='cadastro'),  # (se ainda usar esse)
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
]


