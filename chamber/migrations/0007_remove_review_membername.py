# Generated by Django 3.2.6 on 2022-01-22 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0006_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='memberName',
        ),
    ]
