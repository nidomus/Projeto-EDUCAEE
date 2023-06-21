from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Aluno



class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Aluno
        fields=(
            'id',
            'nome',
            'sexo',
            'data_nascimento',
            'escola_de_origem',
            'serie',
            'turma',
            'nome_responsavel',
            'telefone_responsavel',
            'parentesco',

        )
