# Generated by Django 2.2.17 on 2021-01-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0007_auto_20210114_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='img_profil',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
