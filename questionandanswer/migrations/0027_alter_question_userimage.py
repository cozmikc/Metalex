# Generated by Django 3.2.6 on 2023-02-03 04:38

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0026_alter_question_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='userImage',
            field=models.ImageField(blank=True, null=True, upload_to='questions/images', validators=[backend.validators.validate_file_size]),
        ),
    ]
