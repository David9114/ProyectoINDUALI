# Generated by Django 4.1.5 on 2023-01-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='estado',
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='codIngrediente',
            field=models.CharField(max_length=50, verbose_name='Cod Ingrediente'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='nomIngrediente',
            field=models.CharField(max_length=50, verbose_name='Nom Ingrediente'),
        ),
    ]
