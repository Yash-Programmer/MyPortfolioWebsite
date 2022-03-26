# Generated by Django 3.1.5 on 2021-05-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendsite', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(max_length=5000),
        ),
    ]