# Generated by Django 4.2.1 on 2023-05-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_guias', '0002_agentes_cotizador_fwr_agentes_creador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargas',
            name='ot',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]