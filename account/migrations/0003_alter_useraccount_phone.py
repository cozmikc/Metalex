# Generated by Django 3.2.6 on 2022-02-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_useraccount_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
