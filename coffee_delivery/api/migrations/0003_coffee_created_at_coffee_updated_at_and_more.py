# Generated by Django 4.1.5 on 2023-12-15 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_coffee_table_alter_coffeebean_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='coffeebean',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffeebean',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]