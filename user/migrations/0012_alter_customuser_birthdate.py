# Generated by Django 4.1.3 on 2023-02-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_customuser_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateTimeField(blank=True, default='2000-10-31 13:45:00.000 +0000'),
            preserve_default=False,
        ),
    ]