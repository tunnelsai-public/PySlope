# Generated by Django 3.2.4 on 2022-04-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slope', '0009_auto_20220415_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialmodel',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
