from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Professor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )

class TeamSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Professor
        fields = (
            "telefone",
            "funcao",
        )