# Generated by Django 3.2 on 2022-12-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0008_auto_20221211_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='number_position',
            field=models.SmallIntegerField(unique=True),
        ),
    ]