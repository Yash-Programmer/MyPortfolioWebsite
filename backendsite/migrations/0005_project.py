# Generated by Django 3.1.5 on 2021-05-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendsite', '0004_auto_20210520_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100000)),
                ('src', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
