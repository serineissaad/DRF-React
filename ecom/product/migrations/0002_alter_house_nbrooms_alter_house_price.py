# Generated by Django 4.2 on 2023-04-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='nbrooms',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
