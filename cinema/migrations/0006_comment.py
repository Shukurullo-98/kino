# Generated by Django 5.1.6 on 2025-02-15 16:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_cinema_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Kommentariya')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', verbose_name='Film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kommentchi')),
            ],
            options={
                'verbose_name': 'Kommentariya',
                'verbose_name_plural': 'Kommentariyalar',
            },
        ),
    ]
