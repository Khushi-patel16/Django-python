# Generated by Django 5.0.5 on 2024-06-01 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_news_alter_aboutmodel_icon_des'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]