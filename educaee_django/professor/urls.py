from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import HistoricoViewSet, get_historicos, salvar_historico

router = DefaultRouter()
router.register(r"professores", HistoricoViewSet, basename="professores")

urlpatterns = [
    path("", include(router.urls)),
]