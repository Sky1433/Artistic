# Generated by Django 4.1.3 on 2022-11-15 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='artwork',
        ),
        migrations.DeleteModel(
            name='Artwork',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
