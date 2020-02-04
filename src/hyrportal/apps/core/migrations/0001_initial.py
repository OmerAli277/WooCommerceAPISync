# Generated by Django 2.2.8 on 2020-02-04 17:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('company_name', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('company_vat', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=128, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WooCommerceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=255, null=True)),
                ('consumer_key', models.CharField(blank=True, max_length=255, null=True)),
                ('consumer_secret', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'WooCommerce - Details',
                'verbose_name_plural': 'WooCommerce - Details',
            },
        ),
        migrations.CreateModel(
            name='WooCommerceSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=255, null=True)),
                ('consumer_key', models.CharField(blank=True, max_length=255, null=True)),
                ('consumer_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('is_sync_articles', models.BooleanField(default=False)),
                ('is_post_orders', models.BooleanField(default=False)),
                ('is_post_invoices', models.BooleanField(default=False)),
                ('is_bookkeep', models.BooleanField(default=False)),
                ('acct_domestic_freight', models.CharField(blank=True, max_length=4, null=True)),
                ('acct_international_freight', models.CharField(blank=True, max_length=4, null=True)),
                ('acct_sales_se', models.CharField(blank=True, max_length=255, null=True)),
                ('acct_sales_eu', models.CharField(blank=True, max_length=4, null=True)),
                ('acct_sales_non_eu', models.CharField(blank=True, max_length=4, null=True)),
                ('acct_sales_six_vat', models.CharField(blank=True, max_length=255, null=True)),
                ('acct_sales_twelve_vat', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_term_code', models.CharField(blank=True, max_length=255, null=True)),
                ('price_list', models.CharField(blank=True, max_length=255, null=True)),
                ('is_webshop_article', models.BooleanField(default=False)),
                ('is_stock_goods', models.BooleanField(default=False)),
                ('last_process_date', models.DateField(blank=True, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'WooCommerce - Settings',
                'verbose_name_plural': 'WooCommerce - Settings',
            },
        ),
        migrations.CreateModel(
            name='WooCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('is_paying_customer', models.BooleanField(default=False)),
                ('orders_count', models.IntegerField(blank=True, default=0, null=True)),
                ('total_spent', models.FloatField(blank=True, default=0, null=True)),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WooMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=256)),
                ('value', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WooOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.IntegerField(default=0)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('order_key', models.CharField(blank=True, max_length=255, null=True)),
                ('created_via', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('discount_total', models.FloatField(blank=True, default=0, null=True)),
                ('discount_tax', models.FloatField(blank=True, default=0, null=True)),
                ('shipping_total', models.FloatField(blank=True, default=0, null=True)),
                ('shipping_tax', models.FloatField(blank=True, default=0, null=True)),
                ('cart_tax', models.FloatField(blank=True, default=0, null=True)),
                ('total', models.FloatField(blank=True, default=0, null=True)),
                ('total_tax', models.FloatField(blank=True, default=0, null=True)),
                ('prices_include_tax', models.FloatField(blank=True, default=0, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_method_title', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('date_paid', models.DateTimeField(blank=True, null=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WooCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='WooProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('permalink', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('price_html', models.TextField(blank=True, default=None, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('catalog_visibility', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_status', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_status', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_class', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_class', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_class_id', models.IntegerField(blank=True, null=True)),
                ('backorders', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('regular_price', models.FloatField(blank=True, default=0, null=True)),
                ('sale_price', models.FloatField(blank=True, default=0, null=True)),
                ('total_sales', models.FloatField(blank=True, default=0, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('on_sale', models.BooleanField(default=False)),
                ('purchasable', models.BooleanField(default=False)),
                ('virtual', models.BooleanField(default=False)),
                ('downloadable', models.BooleanField(default=False)),
                ('manage_stock', models.BooleanField(default=False)),
                ('backorders_allowed', models.BooleanField(default=False)),
                ('backordered', models.BooleanField(default=False)),
                ('sold_individually', models.BooleanField(default=False)),
                ('shipping_required', models.BooleanField(default=False)),
                ('shipping_taxable', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('meta_data', models.ManyToManyField(blank=True, to='core.WooMetaData')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WooVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_id', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('regular_price', models.FloatField(blank=True, default=0, null=True)),
                ('sale_price', models.FloatField(blank=True, default=0, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_status', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_class', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_status', models.CharField(blank=True, max_length=255, null=True)),
                ('backorders', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_class', models.CharField(blank=True, max_length=255, null=True)),
                ('on_sale', models.BooleanField(default=False)),
                ('purchasable', models.BooleanField(default=False)),
                ('virtual', models.BooleanField(default=False)),
                ('downloadable', models.BooleanField(default=False)),
                ('manage_stock', models.BooleanField(default=False)),
                ('backorders_allowed', models.BooleanField(default=False)),
                ('backordered', models.BooleanField(default=False)),
                ('shipping_class_id', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('meta_data', models.ManyToManyField(blank=True, to='core.WooMetaData')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WooProduct')),
            ],
        ),
        migrations.CreateModel(
            name='WooOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderitem_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_class', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('subtotal', models.FloatField(blank=True, default=0, null=True)),
                ('subtotal_tax', models.FloatField(blank=True, default=0, null=True)),
                ('total', models.FloatField(blank=True, default=0, null=True)),
                ('total_tax', models.FloatField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='woo_orderitems', to='core.WooOrder')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.WooProduct')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.WooVariant')),
            ],
        ),
        migrations.AddField(
            model_name='woocustomer',
            name='meta_data',
            field=models.ManyToManyField(blank=True, to='core.WooMetaData'),
        ),
        migrations.CreateModel(
            name='WCTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woo_orders', models.IntegerField(blank=True, null=True, verbose_name='WooCommerce Orders')),
                ('customer_created', models.IntegerField(blank=True, null=True, verbose_name='Customer Created')),
                ('unprocess_orders', models.IntegerField(blank=True, null=True, verbose_name='Unprocess Orders')),
                ('created_orders', models.IntegerField(blank=True, null=True, verbose_name='Created Orders')),
                ('created_invoices', models.IntegerField(blank=True, null=True, verbose_name='Created Invoices')),
                ('created_articles', models.IntegerField(blank=True, null=True, verbose_name='Created Articles')),
                ('exists_articles', models.IntegerField(blank=True, null=True, verbose_name='Exists Articles')),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WooCommerce - Transactions',
                'verbose_name_plural': 'WooCommerce - Transactions',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=128)),
                ('customer_name', models.CharField(max_length=128)),
                ('account_type', models.CharField(choices=[('fortnox', 'Fortnox'), ('visma', 'Visma')], max_length=128)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
