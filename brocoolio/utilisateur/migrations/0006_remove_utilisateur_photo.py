# Generated by Django 2.2.17 on 2021-01-13 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0005_auto_20210113_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='photo',
        ),
    ]
