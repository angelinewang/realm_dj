# Generated by Django 4.1.3 on 2023-01-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_customuser_options_alter_customuser_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture_data',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]