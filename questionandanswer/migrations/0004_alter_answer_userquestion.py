# Generated by Django 3.2.6 on 2021-12-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0003_alter_answer_userquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='userquestion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionandanswer.question'),
        ),
    ]