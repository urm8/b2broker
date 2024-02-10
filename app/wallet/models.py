# Create your models here.
from django.db import models
from django.utils.text import gettext_lazy as _


class Wallet(models.Model):
    label = models.CharField(max_length=255, verbose_name=_("Label"), blank=False)
    balance = models.DecimalField(
        _("Balance"), max_digits=18, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _(
            "Wallets"
        )  # some languages have different rules for pluralization
