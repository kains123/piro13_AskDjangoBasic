# Generated by Django 2.0.13 on 2020-07-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]