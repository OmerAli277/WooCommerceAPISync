# Generated by Django 2.2.8 on 2020-02-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200218_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
