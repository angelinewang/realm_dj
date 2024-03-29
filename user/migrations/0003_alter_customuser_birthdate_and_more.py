# Generated by Django 4.1.3 on 2022-12-13 14:35

import django.core.files.storage
from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/profile_pictures'), upload_to='', validators=[user.validators.validate_file_extension]),
        ),
    ]
