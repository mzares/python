# Generated by Django 5.0.2 on 2024-02-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
