# Generated by Django 4.2.16 on 2024-09-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False, help_text='Featured post on home page'),
        ),
    ]
