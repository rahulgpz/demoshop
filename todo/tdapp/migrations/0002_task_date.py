# Generated by Django 4.1.7 on 2023-03-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-09-23'),
            preserve_default=False,
        ),
    ]
