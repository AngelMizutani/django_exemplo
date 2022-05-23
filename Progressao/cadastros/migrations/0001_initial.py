# Generated by Django 4.0.4 on 2022-05-23 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('pontos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('detalhes', models.CharField(max_length=100)),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.campo')),
            ],
        ),
    ]
