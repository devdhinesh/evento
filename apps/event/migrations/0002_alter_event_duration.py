# Generated by Django 4.0.1 on 2022-02-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
