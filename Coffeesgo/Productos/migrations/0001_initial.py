# Generated by Django 3.2.7 on 2021-09-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.FloatField()),
                ('costo', models.FloatField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('categoria', models.CharField(blank=True, choices=[('Café', 'C'), ('Artículos', 'A')], max_length=20, null=True)),
                ('cod_barras', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
