# Generated by Django 2.2.8 on 2021-08-02 22:09

from django.db import migrations, models
import roleplaying.models


class Migration(migrations.Migration):

    dependencies = [
        ('roleplaying', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleplayingitem',
            name='digital_version',
            field=models.FileField(blank=True, null=True, upload_to=roleplaying.models.get_item_image_upload_path),
        ),
    ]
