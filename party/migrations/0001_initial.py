# Generated by Django 4.1.3 on 2022-11-24 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('flat', models.CharField(max_length=50)),
                ('first_entry', models.DateTimeField()),
                ('vibe', models.IntegerField(choices=[(1, 'Chill: 5 - 10 People'), (2, 'Party: 20 - 30 People'), (3, 'Rager: 50+ People')], default=1, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
