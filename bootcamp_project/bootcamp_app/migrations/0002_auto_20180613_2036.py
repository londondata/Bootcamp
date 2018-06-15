# Generated by Django 2.0.5 on 2018-06-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.BooleanField()),
                ('difficulty', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.BooleanField()),
                ('difficulty', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='character',
            name='energy',
        ),
    ]
