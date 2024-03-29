# Generated by Django 4.1.3 on 2022-12-13 16:33

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/profile_pictures'), upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg'])]),
        ),
    ]
