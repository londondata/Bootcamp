# Generated by Django 2.0.5 on 2018-06-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp_app', '0005_auto_20180618_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='finals_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]