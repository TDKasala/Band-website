# Generated by Django 4.2.1 on 2023-06-16 19:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("band", "0003_album_concert_exclusiveevent_song"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="album",
            name="cover_image",
        ),
        migrations.RemoveField(
            model_name="bandmember",
            name="image",
        ),
        migrations.RemoveField(
            model_name="concert",
            name="poster",
        ),
        migrations.RemoveField(
            model_name="exclusiveevent",
            name="poster",
        ),
    ]
