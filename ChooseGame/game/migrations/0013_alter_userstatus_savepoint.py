# Generated by Django 4.0.6 on 2022-08-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_rename_save_userstatus_savepoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='savepoint',
            field=models.CharField(default='beginning_0', max_length=100),
        ),
    ]
