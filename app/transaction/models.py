from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
class Transaction(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Transaction date"), auto_now_add=True
    )
    wallet = models.ForeignKey(
        verbose_name=_("Wallet"),
        to="wallet.Wallet",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    txid = models.CharField(
        max_length=255, verbose_name=_("Transaction identifier"), unique=True
    )
    amount = models.DecimalField(
        verbose_name=_("Amount"), max_digits=18, decimal_places=2
    )

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
