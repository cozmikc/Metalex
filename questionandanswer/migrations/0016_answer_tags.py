# Generated by Django 3.2.6 on 2022-01-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0015_auto_20211231_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
