# Generated by Django 5.0.2 on 2024-02-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="balance",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=18, verbose_name="Balance"
            ),
        ),
    ]