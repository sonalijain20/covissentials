# Generated by Django 3.1.7 on 2021-05-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20210512_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='avail',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
