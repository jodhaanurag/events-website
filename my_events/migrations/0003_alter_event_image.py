# Generated by Django 4.0 on 2022-01-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_events', '0002_alter_event_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]