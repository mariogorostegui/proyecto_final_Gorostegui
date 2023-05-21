# Generated by Django 4.2.1 on 2023-05-21 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_guias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentes',
            name='cotizador_fwr',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='agentes',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentes',
            name='manager_fwr',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='agentes',
            name='operativo_fwe',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='cargas',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
