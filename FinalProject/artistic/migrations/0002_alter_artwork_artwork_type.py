# Generated by Django 4.1.3 on 2022-11-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artwork_type',
            field=models.CharField(choices=[('Painting', 'Painting'), ('Digital', 'Digital'), ('Crafts', 'Crafts')], default='Painting', max_length=64),
        ),
    ]
