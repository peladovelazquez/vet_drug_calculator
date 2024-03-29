# Generated by Django 4.2.9 on 2024-01-05 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_unidaddosis_medicamento_unidad_dosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='unidad_dosis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.unidaddosis'),
        ),
        migrations.AlterField(
            model_name='unidaddosis',
            name='nombre',
            field=models.CharField(blank=True, max_length=7, unique=True),
        ),
    ]
