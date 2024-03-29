# Generated by Django 5.0.2 on 2024-02-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255, verbose_name="Label")),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2, max_digits=18, verbose_name="Balance"
                    ),
                ),
            ],
            options={
                "verbose_name": "Wallet",
                "verbose_name_plural": "Wallets",
            },
        ),
    ]
