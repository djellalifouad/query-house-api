# Generated by Django 4.2 on 2023-04-25 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_query_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='algorithm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joins', to='app.joinalgorithm'),
        ),
        migrations.AlterField(
            model_name='join',
            name='index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joins', to='app.joinindex'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='algorithm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='app.selectionalgorithm'),
        ),
    ]