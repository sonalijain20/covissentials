# Generated by Django 3.1.7 on 2021-05-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='blood_group',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
