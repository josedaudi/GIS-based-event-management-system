# Generated by Django 2.0.4 on 2018-05-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProviders', '0011_auto_20180505_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproviders',
            name='rates',
            field=models.CharField(choices=[('nonStar', 'nonStar'), ('firstStar', 'firstStar'), ('secondStart', 'secondStar'), ('thirdStar', 'thirdStar'), ('fourthStart', 'fourthStart'), ('fifthStart', 'fifthStar')], default='nonStar', max_length=50),
        ),
    ]
