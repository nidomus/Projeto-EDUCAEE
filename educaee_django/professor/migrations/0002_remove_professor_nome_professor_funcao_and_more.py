# Generated by Django 4.2.2 on 2023-06-21 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.AddField(
            model_name='professor',
            name='funcao',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]