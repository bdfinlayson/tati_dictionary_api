# Generated by Django 3.1.7 on 2021-03-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210327_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaryentry',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dictionaryentry',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, default='2021-03-27'),
            preserve_default=False,
        ),
    ]
