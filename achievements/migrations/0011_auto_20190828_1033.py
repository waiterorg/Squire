# Generated by Django 2.2.3 on 2019-08-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0010_auto_20190827_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='claimants',
            field=models.ManyToManyField(blank=True, related_name='claimed_achievements', to='membership_file.Member'),
        ),
    ]
