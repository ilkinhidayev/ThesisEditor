# Generated by Django 4.2.3 on 2023-08-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thesis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tez',
            name='dosya_converted',
            field=models.FileField(blank=True, null=True, upload_to='thesis_converted/'),
        ),
    ]
