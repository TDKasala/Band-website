# Generated by Django 4.2.1 on 2023-06-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("band", "0007_remove_exclusive_content_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="concert_list",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="exclusive_content",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
