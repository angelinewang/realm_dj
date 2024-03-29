# Generated by Django 4.1.3 on 2022-11-24 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('party', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Guest Invited'), (1, 'Guest Confirmed'), (2, 'Guest Canceled'), (3, 'Guest Checked-in'), (4, 'Guest No-showed')], default=0, null=True)),
                ('plus_ones', models.IntegerField(blank=True, default=0, null=True)),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('party_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.party')),
            ],
        ),
    ]
