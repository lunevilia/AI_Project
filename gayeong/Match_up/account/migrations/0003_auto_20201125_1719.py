# Generated by Django 3.1.1 on 2020-11-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201125_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='personnel',
            field=models.PositiveIntegerField(default=0),
        ),
    ]