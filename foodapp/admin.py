
from django.contrib import admin
from .models import customerinfomodel, morningmenu, afternoonmenu, eveningmenu, orderinfo
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname', 'phonenumber', 'location', 'date_joined', 'is_admin', 'is_staff')
    search_fields = ('username', 'email')
    readonly_fields = ('id', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

 

admin.site.register(customerinfomodel, AccountAdmin)
admin.site.register(morningmenu)
admin.site.register(afternoonmenu)
admin.site.register(eveningmenu)
admin.site.register(orderinfo)

