from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class UserAdmin (ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'email', 'telephone')
    list_display_links = ('id', 'email', 'telephone')
    search_fields = ('email', 'telephone')


@admin.register(Storages)
class storagesAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'phone', 'address','boss')
    list_display_links = ('id', 'phone', 'address','boss')

    class Meta:
        proxy = True


@admin.register(Sales)
class salesAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'company','price','number')
    list_display_links = ('id', 'name', 'company','price','number')

    class Meta:
        proxy = True


@admin.register(Companies)
class companiesAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'address','phone')
    list_display_links = ('id', 'name', 'address','phone')

    class Meta:
        proxy = True


@admin.register(Contacts)
class contactsAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','position','birthday', 'address','phone')
    list_display_links = ('id', 'first_name', 'last_name','position','birthday', 'address','phone')

    class Meta:
        proxy = True


@admin.register(Main)
class mainAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'sale', 'number','artist')
    list_display_links = ('id', 'sale', 'number','artist')

    class Meta:
        proxy = True


admin.site.register(User, UserAdmin)

