# Generated by Django 3.1.7 on 2021-12-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendsite', '0011_delete_cert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('cert_id', models.CharField(max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
