# Generated by Django 4.2.4 on 2023-09-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0002_fotografia_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
    ]
