# Generated by Django 5.0.5 on 2024-06-03 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_portfolio_details_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioimage',
            name='portfolio',
        ),
        migrations.DeleteModel(
            name='Portfolio_details',
        ),
        migrations.DeleteModel(
            name='PortfolioImage',
        ),
    ]
