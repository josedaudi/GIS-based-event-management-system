# Generated by Django 2.0.4 on 2018-05-05 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProviders', '0007_serviceproviders_pic_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='name',
        ),
        migrations.AddField(
            model_name='servicename',
            name='service',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='service_name', to='serviceProviders.Services'),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='serviceProviders.ServiceProviders'),
        ),
    ]
