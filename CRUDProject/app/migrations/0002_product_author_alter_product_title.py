# Generated by Django 4.2.4 on 2023-08-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='admin', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
