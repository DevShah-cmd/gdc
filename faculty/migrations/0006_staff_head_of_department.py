# Generated by Django 3.2 on 2022-12-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_auto_20221208_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='head_of_department',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
