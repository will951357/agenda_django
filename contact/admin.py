from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone','category',)
    ordering = ('-id',) # Sinal de  - significa descending
    list_filter = ('created_date',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = 10
    list_max_show_all = 100
    # list_editable = ('first_name',)
    list_display_links = ('id',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)
    list_per_page = 50
    list_max_show_all = 100
    search_fields = ('id', 'name',)