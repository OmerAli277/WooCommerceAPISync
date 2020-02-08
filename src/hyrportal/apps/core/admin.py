from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import WooCustomer, WooProduct, WooOrder, User

admin.site.register(User)

# class MyUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (
#             _('Personal info'),
#             {'fields': ('company_name', 'address',  'company_vat', 'city', 'zip_code')}
#         ),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),s
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     list_display = ('username', 'company_name', 'address', 'is_staff')


# admin.site.register(User, MyUserAdmin)


# @admin.register(Seller)
# class SellerAdmin(admin.ModelAdmin):
#     list_display = ('customer_no', 'customer_name', 'account_type', 'owner')
#     fields = ('customer_no', 'customer_name', 'account_type', 'owner')


@admin.register(WooCustomer)
class WooCustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state',
                    'postcode', 'country', 'email', 'phone')
    fields = ('first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state',
              'postcode', 'country', 'email', 'phone')


@admin.register(WooProduct)
class WooProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'parent_id', 'name', 'slug', 'permalink', 'description', 'short_description', 'sku',
                    'type', 'price_html', 'status', 'catalog_visibility', 'stock_quantity', 'stock_status',
                    'tax_status',
                    'tax_class', 'shipping_class', 'shipping_class_id', 'backorders', 'price', 'regular_price',
                    'sale_price', 'total_sales', 'featured', 'on_sale', 'purchasable', 'virtual', 'downloadable',
                    'manage_stock', 'backorders_allowed', 'backordered', 'sold_individually', 'shipping_required',
                    'shipping_taxable', 'date_created')
    fields = ('product_id', 'parent_id', 'name', 'slug', 'permalink', 'description', 'short_description', 'sku',
              'type', 'price_html', 'status', 'catalog_visibility', 'stock_quantity', 'stock_status', 'tax_status',
              'tax_class', 'shipping_class', 'shipping_class_id', 'backorders', 'price', 'regular_price',
              'sale_price', 'total_sales', 'featured', 'on_sale', 'purchasable', 'virtual', 'downloadable',
              'manage_stock', 'backorders_allowed', 'backordered', 'sold_individually', 'shipping_required',
              'shipping_taxable', 'date_created')


@admin.register(WooOrder)
class WooOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'parent_id', 'number', 'order_key', 'created_via', 'version', 'status', 'currency',
                    'discount_total', 'discount_tax', 'shipping_total', 'shipping_tax', 'cart_tax', 'total',
                    'total_tax',
                    'prices_include_tax', 'payment_method', 'payment_method_title', 'transaction_id', 'date_created',
                    'date_modified', 'date_paid', 'date_completed')

    fields = ('order_id', 'parent_id', 'number', 'order_key', 'created_via', 'version', 'status', 'currency',
              'discount_total', 'discount_tax', 'shipping_total', 'shipping_tax', 'cart_tax', 'total', 'total_tax',
              'prices_include_tax', 'payment_method', 'payment_method_title', 'transaction_id', 'date_created',
              'date_modified', 'date_paid', 'date_completed')
