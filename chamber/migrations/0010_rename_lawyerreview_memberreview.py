# Generated by Django 3.2.6 on 2022-01-22 09:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chamber', '0009_chamber_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LawyerReview',
            new_name='MemberReview',
        ),
    ]