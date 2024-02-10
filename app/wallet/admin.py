# Register your models here.
from django.contrib import admin

from wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    fields = ["label", "balance"]
    readonly_fields = ["balance"]
    search_fields = ["label"]
    list_display = ["id", "label", "balance"]
    list_display_links = ["id", "label"]
