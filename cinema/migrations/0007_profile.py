# Generated by Django 5.1.6 on 2025-02-17 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Profil fotosi')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon raqami')),
                ('about_user', models.CharField(blank=True, max_length=100, null=True, verbose_name='Foydalanuvchi xaqida')),
                ('publisher', models.BooleanField(default=True, verbose_name='Filmga ruxsat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profils',
            },
        ),
    ]
