# Generated by Django 4.2 on 2023-05-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_query_prefix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='execution_time',
            new_name='execution_time_hybride',
        ),
        migrations.AddField(
            model_name='query',
            name='execution_time_pg',
            field=models.FloatField(null=True),
        ),
    ]
