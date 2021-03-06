# Generated by Django 3.1.7 on 2021-05-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('landmark', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
    ]
