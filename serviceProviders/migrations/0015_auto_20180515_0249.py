# Generated by Django 2.0.4 on 2018-05-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProviders', '0014_auto_20180515_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='dislikes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='images',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
