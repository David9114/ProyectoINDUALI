# Generated by Django 4.1.1 on 2023-02-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_remove_receta_consecutivo_receta_fkcodingrediente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='fkcodComponente',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='fkcodIngrediente',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='super',
        ),
        migrations.AddField(
            model_name='receta',
            name='preparacion',
            field=models.TextField(null=True, verbose_name='Preparación'),
        ),
    ]