# Generated by Django 5.0.6 on 2025-03-05 11:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('imageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('imageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(max_length=550)),
                ('is_featured', models.BooleanField(default=False)),
                ('clothesType', models.CharField(default='unisex', max_length=255)),
                ('rating', models.FloatField(default=1.0)),
                ('colors', models.JSONField(blank=True)),
                ('sizes', models.JSONField(blank=True)),
                ('imageUrls', models.JSONField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
