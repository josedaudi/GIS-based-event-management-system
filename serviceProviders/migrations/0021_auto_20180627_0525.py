# Generated by Django 2.0.4 on 2018-06-27 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProviders', '0020_auto_20180627_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecomments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='serviceProviders.Images'),
        ),
    ]
