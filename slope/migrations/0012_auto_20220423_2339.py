# Generated by Django 3.2.4 on 2022-04-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slope', '0011_limitsmodel_watertablemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limitsmodel',
            name='left_x_right',
            field=models.FloatField(default=4),
        ),
        migrations.AlterField(
            model_name='limitsmodel',
            name='right_x',
            field=models.FloatField(default=8),
        ),
        migrations.AlterField(
            model_name='limitsmodel',
            name='right_x_left',
            field=models.FloatField(default=6),
        ),
    ]
