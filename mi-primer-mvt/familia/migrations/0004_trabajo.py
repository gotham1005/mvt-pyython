# Generated by Django 4.0.4 on 2022-05-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0003_persona_altura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmpresa', models.CharField(max_length=100)),
                ('direccionEmpresa', models.CharField(max_length=100)),
                ('rubroEmpresa', models.CharField(max_length=100)),
            ],
        ),
    ]