from django.shortcuts import render
from rest_framework import viewsets
from .models import Professor
from .serializers import ProfessorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core import serializers


# Create your views here.
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filters = ()

    def get_queryset(self):

        return self.queryset

    def perform_create(self, serializer):
        serializer.save()




