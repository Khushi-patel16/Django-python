# Generated by Django 5.0.5 on 2024-06-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_portfolio_details_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_details',
            name='images',
            field=models.JSONField(default=dict),
        ),
    ]
