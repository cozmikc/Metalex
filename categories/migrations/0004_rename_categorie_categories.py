# Generated by Django 3.2.6 on 2021-12-26 12:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0003_rename_categories_categorie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Categories',
        ),
    ]