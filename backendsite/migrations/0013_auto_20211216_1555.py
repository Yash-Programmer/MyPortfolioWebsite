# Generated by Django 3.1.7 on 2021-12-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendsite', '0012_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification_I',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_II',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_III',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_IV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_V',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Certification_VI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('certificate_id', models.CharField(blank=True, default='Not Provided', max_length=1000000)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
    ]