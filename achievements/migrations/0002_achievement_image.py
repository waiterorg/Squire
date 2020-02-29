# Generated by Django 2.2.3 on 2020-02-29 21:42

import achievements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='image',
            field=models.ImageField(default=1, upload_to=achievements.models.get_upload_path),
            preserve_default=False,
        ),
    ]
