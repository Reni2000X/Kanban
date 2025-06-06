# Generated by Django 5.1.6 on 2025-02-24 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='dashboard.board')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('voice', models.CharField(blank=True, max_length=255)),
                ('script', models.CharField(blank=True, max_length=255)),
                ('lines', models.IntegerField(default=0)),
                ('recorded_lines', models.IntegerField(default=0)),
                ('remaining_lines', models.IntegerField(default=0)),
                ('recorded_total', models.IntegerField(default=0)),
                ('origin_id', models.CharField(blank=True, max_length=255, null=True)),
                ('base_name', models.CharField(blank=True, max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='dashboard.group')),
            ],
        ),
    ]
