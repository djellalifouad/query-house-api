# Generated by Django 4.2 on 2023-05-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_query_join_order1_query_join_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='choosed_plan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
