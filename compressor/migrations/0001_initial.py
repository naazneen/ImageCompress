# Generated by Django 3.0.2 on 2020-01-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(null=True, upload_to='original/', verbose_name='')),
                ('converted', models.FileField(null=True, upload_to='converted/', verbose_name='')),
            ],
        ),
    ]
