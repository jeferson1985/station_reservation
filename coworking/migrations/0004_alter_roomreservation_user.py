# Generated by Django 4.2.1 on 2023-05-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0003_alter_rooms_options_roomreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreservation',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
