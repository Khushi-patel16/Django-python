# Generated by Django 5.0.5 on 2024-06-01 04:43

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_counts_remove_features_counter_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='icon_des',
            field=tinymce.models.HTMLField(),
        ),
    ]
