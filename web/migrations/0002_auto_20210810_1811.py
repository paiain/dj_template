# Generated by Django 3.2.5 on 2021-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_cteated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]