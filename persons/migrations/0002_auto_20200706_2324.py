# Generated by Django 3.0.6 on 2020-07-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdaye',
            field=models.DateField(blank=True, null=True),
        ),
    ]
