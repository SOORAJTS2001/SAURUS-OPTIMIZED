# Generated by Django 3.1.7 on 2021-05-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_edx', '0004_collegereg'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeSignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
