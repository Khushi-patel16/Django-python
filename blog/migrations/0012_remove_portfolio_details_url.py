# Generated by Django 5.0.5 on 2024-06-01 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_portfolio_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='details_url',
        ),
    ]