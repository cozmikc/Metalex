# Generated by Django 3.2.6 on 2022-02-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_bookmarkedlawyer_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkedlawyer',
            name='color',
        ),
    ]
