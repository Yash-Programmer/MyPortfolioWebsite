# Generated by Django 3.1.7 on 2021-12-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendsite', '0009_certificate_certificate_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
