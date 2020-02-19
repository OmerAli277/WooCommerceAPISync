from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser , UserManager
from django.db import models


class User(AbstractUser):

    company_name = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    company_vat = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    zip_code = models.CharField(max_length=128, null=True, blank=True)
    FORTNOX = 'fortnox'
    VISMA = 'visma'

    ACCOUNT_TYPES = [
        (FORTNOX, 'Fortnox'),
        (VISMA, 'Visma'),
    ]
    customer_no = models.CharField(max_length=128, null=True, blank=True, unique=True)
    customer_name = models.CharField(max_length=128, null=True, blank=True)
    account_type = models.CharField(max_length=128, choices=ACCOUNT_TYPES)
    is_super_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)



class WooMetaData(models.Model):
    key = models.CharField(max_length=256, db_index=True)
    value = models.TextField(default=None, null=True, blank=True)
    #
    # def __str__(self):
    #     return f"{self.key} : {self.value}"

#
class WooCustomerBilling(models.Model):
    customer = models.ForeignKey('WooCustomer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

class WooCustomerShipping(models.Model):
    customer = models.ForeignKey('WooCustomer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

class WooCustomer(models.Model):
    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    is_paying_customer = models.BooleanField(default=False)
    meta_data = models.ManyToManyField(to='WooMetaData', blank=True)
    customer_id = models.IntegerField(null=True, blank=True, unique=True)

    email = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return f"{self.last_name}, {self.first_name}"


class WooOrder(models.Model):
    customer = models.ForeignKey('WooCustomer', on_delete=models.CASCADE)
    order_id = models.IntegerField(null=True, blank=True, unique=True)
    parent_id = models.IntegerField(default=0)
    number = models.CharField(max_length=255, null=True, blank=True)
    order_key = models.CharField(max_length=255, null=True, blank=True)
    created_via = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)

    discount_total = models.CharField(max_length=255, null=True, blank=True)
    discount_tax = models.CharField(max_length=255, null=True, blank=True)
    shipping_total = models.CharField(max_length=255, null=True, blank=True)
    shipping_tax = models.CharField(max_length=255, null=True, blank=True)
    cart_tax = models.CharField(max_length=255, null=True, blank=True)
    total = models.CharField(max_length=255, null=True, blank=True)
    total_tax = models.CharField(max_length=255, null=True, blank=True)
    prices_include_tax = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    payment_method_title = models.CharField(max_length=255, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    # customer_id = models.IntegerField(null=True, blank=True)    #new entity added in DB
    customer_ip_address = models.CharField(max_length=255, null=True, blank=True)
    customer_note = models.CharField(max_length=255, null=True, blank=True)

    # billing = models.ForeignKey(to='WooBilling', blank=True, null=True, on_delete=models.SET_NULL)
    # shipping = models.ForeignKey(to='WooShippment', blank=True, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
    date_paid = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
   



class WooOrderItem(models.Model):
    order = models.ForeignKey(to='WooOrder', related_name='woo_orderitems', on_delete=models.CASCADE)
    # subscription = models.ForeignKey(to=WooSubscription, null=True, blank=True, on_delete=models.SET_NULL)
    orderitem_id = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    tax_class = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    subtotal = models.FloatField(null=True, blank=True, default=0)
    subtotal_tax = models.FloatField(null=True, blank=True, default=0)
    total = models.FloatField(null=True, blank=True, default=0)
    total_tax = models.FloatField(null=True, blank=True, default=0)


    # order_id = models.IntegerField(null=True, blank=True, unique=True)
    id_order = models.IntegerField(null=True, blank=True)

    product = models.ForeignKey(to='WooProduct', null=True, blank=True, on_delete=models.SET_NULL)
    variant = models.ForeignKey(to='WooVariant', null=True, blank=True, on_delete=models.SET_NULL)





class WooProduct(models.Model):
    product_id = models.IntegerField(unique=True, default=0)
    parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
    permalink = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    price_html = models.TextField(default=None, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    catalog_visibility = models.CharField(max_length=255, null=True, blank=True)
    stock_quantity = models.CharField(max_length=255, null=True, blank=True)
    stock_status = models.CharField(max_length=255, null=True, blank=True)
    tax_status = models.CharField(max_length=255, null=True, blank=True)
    tax_class = models.CharField(max_length=255, null=True, blank=True)
    shipping_class = models.CharField(max_length=255, null=True, blank=True)
    shipping_class_id = models.IntegerField(null=True, blank=True)
    backorders = models.CharField(max_length=255, null=True, blank=True)

    price = models.CharField(max_length=255, null=True, blank=True, default=0)
    regular_price = models.CharField(max_length=255, null=True, blank=True, default=0)
    sale_price = models.CharField(max_length=255, null=True, blank=True, default=0)
    total_sales = models.CharField(max_length=255, null=True, blank=True, default=0)

    featured = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    purchasable = models.BooleanField(default=False)
    virtual = models.BooleanField(default=False)
    downloadable = models.BooleanField(default=False)
    manage_stock = models.BooleanField(default=False)
    backorders_allowed = models.BooleanField(default=False)
    backordered = models.BooleanField(default=False)
    sold_individually = models.BooleanField(default=False)
    shipping_required = models.BooleanField(default=False)
    shipping_taxable = models.BooleanField(default=False)
    meta_data = models.ManyToManyField(to='WooMetaData', blank=True)

    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)
  

    # def __str__(self):
    #     return self.product_id

    class Meta:
        ordering = ('name',)


class WooVariant(models.Model):
    products = models.ForeignKey(to='WooProduct', on_delete=models.CASCADE)
    variant_id = models.IntegerField(null=True, blank=True, unique=True)
    description = models.TextField(default=None, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    regular_price = models.FloatField(null=True, blank=True, default=0)
    sale_price = models.FloatField(null=True, blank=True, default=0)
    status = models.CharField(max_length=255, null=True, blank=True)
    tax_status = models.CharField(max_length=255, null=True, blank=True)
    tax_class = models.CharField(max_length=255, null=True, blank=True)
    stock_quantity = models.CharField(max_length=255, null=True, blank=True)
    stock_status = models.CharField(max_length=255, null=True, blank=True)
    backorders = models.CharField(max_length=255, null=True, blank=True)
    shipping_class = models.CharField(max_length=255, null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    purchasable = models.BooleanField(default=False)
    virtual = models.BooleanField(default=False)
    downloadable = models.BooleanField(default=False)
    manage_stock = models.BooleanField(default=False)
    backorders_allowed = models.BooleanField(default=False)
    backordered = models.BooleanField(default=False)
    shipping_class_id = models.IntegerField(null=True, blank=True)
    meta_data = models.ManyToManyField(to='WooMetaData', blank=True)
    date_created = models.DateTimeField(null=True, blank=True)




#User settings
class WooCommerceSettings(models.Model):
    # subscription_settings = models.OneToOneField(
    #     to='core.SubscriptionSettings',
    #     unique=True,
    #     related_name='woocommerce_settings',
    #     on_delete=models.CASCADE)

    host = models.CharField(max_length=255, blank=True, null=True)
    consumer_key = models.CharField(max_length=255, blank=True, null=True)
    consumer_secret = models.CharField(max_length=255, blank=True, null=True)
    # version = models.CharField(choices=WooCommerceVersion.choices(), max_length=255, blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    #user may choose if they want their woo orders posted as invoices OR orders in Forntox/Visma
    is_sync_articles = models.BooleanField(default=False)
    is_post_orders = models.BooleanField(default=False)
    is_post_invoices = models.BooleanField(default=False)
    is_bookkeep = models.BooleanField(default=False)
  
    # Fortnox cccounting sales account the user inputs in settings and is used to post invoices/orders 
    acct_domestic_freight = models.CharField(max_length=4, blank=True, null=True)
    acct_international_freight = models.CharField(max_length=4, blank=True, null=True)
    acct_sales_se = models.CharField(max_length=255, blank=True, null=True)
    acct_sales_eu = models.CharField(max_length=4, blank=True, null=True)
    acct_sales_non_eu = models.CharField(max_length=4, blank=True, null=True)
    acct_sales_six_vat = models.CharField(max_length=255, blank=True, null=True)
    acct_sales_twelve_vat = models.CharField(max_length=255, blank=True, null=True)

    #Fortnox parameters for article
    unit_id = models.CharField(max_length=255, blank=True, null=True)
    payment_term_code = models.CharField(max_length=255, blank=True, null=True)
    price_list = models.CharField(max_length=255, blank=True, null=True)
    # vat_rate = models.CharField(choices=VatRates.choices(), default=VatRates.VAT_25, max_length=255)

    # Visma parameters for article_info
    is_webshop_article = models.BooleanField(default=False)
    is_stock_goods = models.BooleanField(default=False)
    # article_type = models.CharField(choices=ArticleTypes.choices(), max_length=255, blank=True, null=True)

    #last date script processed order and booked in accounting software
    last_process_date = models.DateField(null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('WooCommerce - Settings')
        verbose_name_plural = _('WooCommerce - Settings')

    # def __str__(self):
    #     return f"[{self.subscription_settings}] - {self.id}"

class fortnoxApiDetails(models.Model):
    seller_id = models.ForeignKey(to='User', on_delete=models.CASCADE,  null=False, default='')
    client_secret = models.CharField(max_length=255, default='', null=False)
    access_token = models.CharField(max_length=255, default='', null=False)
    authorization_Code = models.CharField(max_length=255, default='', null=False)

class WooCommerceDetails(models.Model):
    host = models.CharField(max_length=255, blank=True, null=True)
    consumer_key = models.CharField(max_length=255, blank=True, null=True)
    consumer_secret = models.CharField(max_length=255, blank=True, null=True)
    # version = models.CharField(choices=WooCommerceVersion.choices(), max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('WooCommerce - Details')
        verbose_name_plural = _('WooCommerce - Details')


#store transactions in DB in order to keep log of what has been processed for user
class WCTransactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # subscription = models.ForeignKey(to="core.Subscription", related_name="wc_transactions", blank=True, null=True, on_delete=models.SET_NULL)
    # accounting_type = models.SmallIntegerField(choices=AccountingType.choices(), blank=True, null=True)
    woo_orders = models.IntegerField("WooCommerce Orders", null=True, blank=True)
    customer_created = models.IntegerField("Customer Created", null=True, blank=True)
    unprocess_orders = models.IntegerField("Unprocess Orders", null=True, blank=True)
    created_orders = models.IntegerField("Created Orders", null=True, blank=True)
    created_invoices = models.IntegerField("Created Invoices", null=True, blank=True)
    created_articles = models.IntegerField("Created Articles", null=True, blank=True)
    exists_articles = models.IntegerField("Exists Articles", null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = _('WooCommerce - Transactions')
        verbose_name_plural = _('WooCommerce - Transactions')

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.update = datetime.today()
        super(WCTransactions, self).save(*args, **kwargs)
