# Generated by Django 2.0.13 on 2020-07-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
