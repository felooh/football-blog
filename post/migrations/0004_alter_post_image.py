# Generated by Django 4.2.2 on 2023-06-27 13:11

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=post.models.get_upload_path
            ),
        ),
    ]
