from django.db import models
from django.db.models import F
from django.db.transaction import atomic
from django.utils.text import gettext_lazy as _

from wallet.models import Wallet


# Create your models here.
class Transaction(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Transaction date"), auto_now_add=True, db_index=True
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

    def __str__(self):
        return f"{self.txid}({self.amount})"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        with atomic():
            if self._state.adding:
                wallet = (
                    Wallet.objects.filter(pk=self.wallet.pk).select_for_update().first()
                )
                super().save(force_insert, force_update, using, update_fields)
                wallet.balance = F("balance") + self.amount
                wallet.save(update_fields=["balance"])

    def delete(self, using=None, keep_parents=False):
        with atomic():
            wallet = (
                Wallet.objects.filter(pk=self.wallet.pk).select_for_update().first()
            )
            wallet.balance = F("balance") - self.amount
            return super().delete(using, keep_parents)
