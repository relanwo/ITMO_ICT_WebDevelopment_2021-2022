# Generated by Django 3.2.8 on 2021-12-08 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_auto_20211208_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='books_new',
        ),
        migrations.RemoveField(
            model_name='report',
            name='readers_new',
        ),
        migrations.RemoveField(
            model_name='report',
            name='readers_total',
        ),
    ]