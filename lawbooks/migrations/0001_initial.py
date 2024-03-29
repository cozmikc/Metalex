# Generated by Django 3.2.6 on 2022-01-08 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LawBook',
            fields=[
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('isBookmarked', models.BooleanField(default=False)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lawbooks.lawbook')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]