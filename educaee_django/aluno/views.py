from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filters = ()

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        serializer.save()




