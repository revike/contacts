# Generated by Django 4.2.4 on 2023-08-24 15:31

import contact.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='last name')),
                ('phone', models.CharField(max_length=16, validators=[contact.validators.validate_phone], verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]