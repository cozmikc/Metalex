# Generated by Django 3.2.6 on 2022-02-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20220209_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarkedlawyer',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]