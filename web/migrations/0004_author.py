# Generated by Django 3.2.5 on 2021-08-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blog_catgory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.IntegerField(choices=[(1, 'นาย'), (2, 'นางสาว'), (3, 'นาง')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
