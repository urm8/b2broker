# Register your models here.
from django.contrib import admin

from wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    fields = '__all__'
    search_fields = ['label']
    list_display = ['id', 'label', 'balance']
    list_display_links = ['id', 'label']
