# Generated by Django 4.0.3 on 2022-09-16 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leetcode', models.URLField(max_length=150)),
                ('Github', models.URLField(max_length=150)),
                ('Hackerrank', models.URLField(max_length=150)),
                ('Coder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
