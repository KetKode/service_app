# Generated by Django 3.2.16 on 2024-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_subscription_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="comment",
            field=models.CharField(default="", max_length=50),
        ),
    ]
