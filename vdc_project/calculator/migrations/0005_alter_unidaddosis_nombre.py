# Generated by Django 4.2.9 on 2024-01-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_medicamento_unidad_dosis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidaddosis',
            name='nombre',
            field=models.CharField(max_length=7),
        ),
    ]