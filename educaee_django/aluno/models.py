from django.db import models


class Aluno(models.Model):
    
    MASCULINO = 'F'
    FEMININO = 'M'
 
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=[(MASCULINO,'Masculino'),(FEMININO,'Feminino')])
    data_nascimento = models.DateField()

    escola_de_origem = models.CharField(max_length=255)

    serie = models.CharField(max_length=3, null=True)
    turma = models.CharField(max_length=1, null=True)

    nome_responsavel = models.CharField(max_length=255)
    telefone_responsavel = models.CharField(max_length=13)
    parentesco = models.CharField(max_length=255)