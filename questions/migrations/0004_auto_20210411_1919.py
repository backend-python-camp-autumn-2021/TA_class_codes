# Generated by Django 3.1 on 2021-04-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210411_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
