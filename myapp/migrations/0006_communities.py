# Generated by Django 4.1.6 on 2024-07-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_blog_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Communities",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="communities"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
