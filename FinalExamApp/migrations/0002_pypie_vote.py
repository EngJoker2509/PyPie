# Generated by Django 3.0 on 2023-01-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAndRegAPP', '0002_auto_20230106_1456'),
        ('FinalExamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pypie',
            name='vote',
            field=models.ManyToManyField(related_name='votes', to='LoginAndRegAPP.User'),
        ),
    ]