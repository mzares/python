# Generated by Django 5.0.2 on 2024-02-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_headline_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]