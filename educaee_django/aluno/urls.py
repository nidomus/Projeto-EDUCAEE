from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AlunoSerializer

router = DefaultRouter()
router.register(r"alunos", AlunoSerializer, basename="alunos")

urlpatterns = [
    path("", include(router.urls)),
]