# Generated by Django 5.0.5 on 2024-06-03 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_portfolio_details_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio_details',
            name='images',
        ),
    ]
