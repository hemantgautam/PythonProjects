# Generated by Django 3.0.4 on 2020-03-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0007_auto_20200313_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='board_url',
            field=models.SlugField(max_length=20),
        ),
    ]
