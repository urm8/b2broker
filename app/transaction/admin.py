# Register your models here.
from django.contrib import admin

from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ["wallet", "txid", "amount"]
    autocomplete_fields = ["wallet"]
    search_fields = ["txid"]
    list_filter = ["wallet"]
