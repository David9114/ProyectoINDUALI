# Generated by Django 4.1.1 on 2023-06-10 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('componente', '0001_initial'),
        ('receta', '0009_remove_receta_codingrediente_receta_nomingrediente'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='nomComponente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='componente.componente', verbose_name='Nombre Componente'),
        ),
    ]
