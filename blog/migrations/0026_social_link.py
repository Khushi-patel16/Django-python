# Generated by Django 5.0.5 on 2024-06-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_footer_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='link',
            field=models.CharField(default='#', max_length=300),
        ),
    ]