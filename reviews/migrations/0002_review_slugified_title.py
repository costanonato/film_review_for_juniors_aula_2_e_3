# Generated by Django 5.0.1 on 2024-01-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slugified_title',
            field=models.SlugField(default='nnn', max_length=200, unique_for_date='published_at'),
            preserve_default=False,
        ),
    ]
