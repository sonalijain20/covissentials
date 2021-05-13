# Generated by Django 3.1.7 on 2021-05-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('msg', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]