# Generated by Django 4.2.2 on 2023-06-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogger", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
