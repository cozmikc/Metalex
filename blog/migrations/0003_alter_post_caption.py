# Generated by Django 3.2.6 on 2022-02-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
