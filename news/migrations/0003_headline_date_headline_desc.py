# Generated by Django 5.0.2 on 2024-02-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_headline_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='headline',
            name='desc',
            field=models.CharField(max_length=700, null=True),
        ),
    ]
