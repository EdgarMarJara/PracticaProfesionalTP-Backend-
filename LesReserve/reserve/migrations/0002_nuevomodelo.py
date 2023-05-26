# Generated by Django 4.2 on 2023-05-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NuevoModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'test_modelo',
            },
        ),
    ]
