# Generated by Django 5.1.6 on 2025-03-18 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('startapp_books', '0003_alter_films_options_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='❌', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice_films', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startapp_books.films')),
            ],
        ),
    ]
