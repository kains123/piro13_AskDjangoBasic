# Generated by Django 2.0.13 on 2020-07-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_name'),
    ]
    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.CharField(max_length=20),
        ),
    ]
