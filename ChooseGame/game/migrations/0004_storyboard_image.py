# Generated by Django 4.0.6 on 2022-07-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_rename_content_choice_storyboard_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyboard',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
