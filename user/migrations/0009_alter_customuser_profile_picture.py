# Generated by Django 4.1.3 on 2023-01-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_customuser_profile_picture_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]