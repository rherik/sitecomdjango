# Generated by Django 4.0.5 on 2022-07-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listadosfilmes',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
