# Generated by Django 4.1.5 on 2023-01-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAndRegAPP', '0002_auto_20230106_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
