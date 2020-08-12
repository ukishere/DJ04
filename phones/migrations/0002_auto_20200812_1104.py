# Generated by Django 2.2.10 on 2020-08-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.TextField(choices=[('iphone-x', 'Iphone X'), ('samsung-galaxy-edge-2', 'Samsung Galaxy Edge 2'), ('nokia-8', 'Nokia 8')], null=True),
        ),
    ]