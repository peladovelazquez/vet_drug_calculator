# Generated by Django 4.2.9 on 2024-01-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='contraindicaciones',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]