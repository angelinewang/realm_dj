# Generated by Django 4.1.3 on 2022-11-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
