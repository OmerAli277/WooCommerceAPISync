# Generated by Django 2.2.8 on 2020-02-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_merge_20200219_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, choices=[('fortnox', 'Fortnox'), ('visma', 'Visma')], max_length=128),
        ),
    ]
