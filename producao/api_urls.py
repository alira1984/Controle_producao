from rest_framework.routers import DefaultRouter
from .views import MaquinaViewSet, TurnoViewSet, ProducaoDiariaViewSet

router = DefaultRouter()
router.register(r'maquinas', MaquinaViewSet)
router.register(r'turnos', TurnoViewSet)
router.register(r'producao', ProducaoDiariaViewSet)

urlpatterns = router.urls
