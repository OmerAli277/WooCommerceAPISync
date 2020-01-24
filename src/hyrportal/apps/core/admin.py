from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Seller


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Personal info'),
            {'fields': ('full_name', 'company_name', 'address',  'company_vat', 'city', 'zip_code')}
        ),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'full_name', 'company_name', 'address', 'is_staff')


admin.site.register(User, MyUserAdmin)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('customer_no', 'customer_name', 'account_type', 'owner')
    fields = ('customer_no', 'customer_name', 'account_type', 'owner')
