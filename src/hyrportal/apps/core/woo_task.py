import json
import requests
from woocommerce import API
# from .models import User, WooCustomer, WooOrder, WooProduct, WooVariant, fortnoxApiDetails, WooCustomerShipping, WooCustomerBilling
from hyrportal.apps.core.models import User, WooCustomer, WooOrder, WooOrderItem, WooProduct, WooVariant, WooCustomerShipping, WooCustomerBilling ,fortnoxApiDetails
from .fn_client import fn_article_api, fn_customer_api, fn_invoice_api, fn_invoice_payment_api
from django.db import DatabaseError

class woo_fn_sync:

    def __init__(self, p_url, p_consumer_key, p_consumer_secret):
        self.wcapi = API(
            url = p_url,
            consumer_key = p_consumer_key,
            consumer_secret = p_consumer_secret,
            version = "wc/v3",
            timeout = 30
        )

    def fortnox_authentication(self, seller_id):
        client_secret = None
        access_token = None
        # if value exist in database=>fortnoxApiDetails:
        #     Use it
        # else:
        #     data = None
        #     # Database call for authentication and secret
        #     try:
        #         r = requests.get(
        #             url="https://api.fortnox.se/3/invoices",
        #             headers = {
        #                 "Authorization-Code": self.Access_Token,
        #                 "Client-Secret":self.Client_Secret,
        #                 "Content-Type":"application/json",
        #                 "Accept":"application/json",
        #             },
        #         )
        #         print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
        #         # print('Response HTTP Response Body : {content}'.format(content=r.content))
        #         data = json.loads(r.content)
        #         access_token = data['access-token']
        #     except requests.exceptions.RequestException as e:
        #         print('fn_authentication HTTP Request failed')
        return client_secret, access_token

    def sync_products(self):
        r = self.wcapi.get("products")
        products = r.json()
        
        try:
            local_products = WooProduct.objects.values('product_id')

            local_ids = {}
            for lp in local_products:
                local_ids[lp['product_id']] = {'exist': False, 'id':lp['product_id']}

            for wp in products:
                if local_ids.get(wp['id']) != None: # Exist in both local and woocomerce
                    local_ids[wp['id']]['exist'] = True
                    local_p = WooProduct.objects.get(product_id=wp['id'])
                    if (local_p != None) and (wp['date_modified'] != local_p.date_modified):
                        # Updata the local Product
                        local_p.product_id = wp['id'] 
                        local_p.parent_id = wp['parent_id']
                        local_p.name = wp['name']
                        local_p.slug = wp['slug'] 
                        local_p.permalink = wp['permalink'] 
                        local_p.description = wp['description'] 
                        local_p.short_description = wp['short_description'] 
                        local_p.sku = wp['sku']
                        local_p.type = wp['type'] 
                        local_p.price_html  = wp['price_html']  
                        local_p.status = wp['status']
                        local_p.catalog_visibility = wp['catalog_visibility'] 
                        local_p.stock_quantity = wp['stock_quantity']
                        local_p.stock_status = wp['stock_status']
                        local_p.tax_status = wp['tax_status']
                        local_p.tax_class = wp['tax_class']
                        local_p.shipping_class = wp['shipping_class'] 
                        local_p.shipping_class_id = wp['shipping_class_id'] 
                        local_p.backorders = wp['backorders']

                        local_p.price = wp['price']
                        local_p.regular_price = wp['regular_price']
                        local_p.sale_price = wp['sale_price']
                        local_p.total_sales = wp['total_sales'] 
                        
                        local_p.featured = wp['featured']
                        local_p.on_sale = wp['on_sale']
                        local_p.purchasable = wp['purchasable'] 
                        local_p.virtual =wp['virtual']
                        local_p.downloadable =wp['downloadable']  
                        local_p.manage_stock = wp['manage_stock'] 
                        local_p.backorders_allowed= wp['backorders_allowed']
                        local_p.backordered = wp['backordered']
                        local_p.sold_individually = wp['sold_individually'] 
                        local_p.shipping_required = wp['shipping_required']
                        local_p.save()
                else: # Does not exist in local, but exist in woocomerce
                    new_product = WooProduct.objects.create(
                        product_id = wp['id'] ,
                        parent_id = wp['parent_id'], 
                        name = wp['name'], 
                        slug = wp['slug'] ,
                        permalink = wp['permalink'], 
                        description = wp['description'], 
                        short_description = wp['short_description'], 
                        sku = wp['sku'], 
                        type = wp['type'], 
                        price_html  = wp['price_html'] , 
                        status = wp['status'],
                        catalog_visibility = wp['catalog_visibility'], 
                        stock_quantity = wp['stock_quantity'], 
                        stock_status = wp['stock_status'], 
                        tax_status = wp['tax_status'], 
                        tax_class = wp['tax_class'],
                        shipping_class = wp['shipping_class'], 
                        shipping_class_id = wp['shipping_class_id'], 
                        backorders = wp['backorders'], 

                        price = wp['price'], 
                        regular_price = wp['regular_price'], 
                        sale_price = wp['sale_price'], 
                        total_sales = wp['total_sales'], 
                        
                        featured = wp['featured'], 
                        on_sale = wp['on_sale'], 
                        purchasable = wp['purchasable'], 
                        virtual =wp['virtual'],
                        downloadable =wp['downloadable'] , 
                        manage_stock = wp['manage_stock'], 
                        backorders_allowed= wp['backorders_allowed'] ,
                        backordered = wp['backordered'], 
                        sold_individually = wp['sold_individually'], 
                        shipping_required = wp['shipping_required']
                        # shipping_taxable= wp['shipping_taxable']
                        # meta_data = wp['meta_data'], 
                        # date_created = wp['date_created']
                        )
                    new_product.save()

            for lp in local_ids:
                if lp['exist'] == False: # Delete products which are not avialable in woocommerce
                    WooProduct.objects.filter(product_id=lp['id']).delete()

        except DatabaseError as e:
            print('Database error: ' + str(e)) 

    def sync_orders(self):
        r = self.wcapi.get("orders")
        orders = r.json()
        print ('In sync_orders')
        try :
            local_orders = WooOrder.objects.values('order_id')
            print(local_orders)

            local_ids = {}
            for lp in local_orders:
                local_ids[lp['order_id']] = {'exist': False, 'id':lp['order_id']}

            for WO in orders:
                if local_ids.get(WO['id']) != None: # Exist in both local and woocomerce
                    local_ids[WO['id']]['exist'] = True
                    local_p = WooOrder.objects.get(order_id=WO['id'])
                    if (local_p != None) and (WO['date_modified'] != local_p.date_modified):
                        # Updata the local Product
                        local_p.order_id = WO['id']
                        local_p.parent_id = WO['parent_id']
                        local_p.number = WO['number']
                        local_p.order_key =  WO['order_key']
                        local_p.created_via =  WO['created_via']
                        local_p.version =  WO['version']
                        local_p.status =  WO['status']
                        local_p.currency =  WO['currency']
                        local_p.discount_total = WO['discount_total']
                        local_p.discount_tax =  WO['discount_tax']
                        local_p.shipping_total =  WO['shipping_total']
                        local_p.shipping_tax =  WO['shipping_tax']
                        local_p.cart_tax =  WO['cart_tax']
                        local_p.total =  WO['total']
                        local_p.total_tax =  WO['total_tax']
                        local_p.prices_include_tax =  WO['prices_include_tax']
                        local_p.payment_method =  WO['payment_method']
                        local_p.payment_method_title = WO['payment_method_title']
                        local_p.transaction_id =  WO['transaction_id']

                        local_p.date_modified = WO['date_modified']
                        local_p.date_paid = WO['date_paid']
                        local_p.date_completed = WO['date_completed']

                        local_p.save()
                else: # Does not exist in local, but exist in woocomerce
                     new_order = WooOrder.objects.create(
                        order_id = WO['id'],
                        parent_id = WO['parent_id'],
                        number = WO['number'],
                        order_key =  WO['order_key'],
                        created_via =  WO['created_via'],
                        version =  WO['version'],
                        status =  WO['status'],
                        currency =  WO['currency'],
                        discount_total = WO['discount_total'],
                        discount_tax =  WO['discount_tax'],
                        shipping_total =  WO['shipping_total'],
                        shipping_tax =  WO['shipping_tax'],
                        cart_tax =  WO['cart_tax'],
                        total =  WO['total'],
                        total_tax =  WO['total_tax'],
                        prices_include_tax =  WO['prices_include_tax'],
                        payment_method =  WO['payment_method'],
                        payment_method_title = WO['payment_method_title'],
                        transaction_id =  WO['transaction_id'],

                        date_created = WO['date_created'],
                        date_modified = WO['date_modified'],
                        date_paid = WO['date_paid'],
                        date_completed = WO['date_completed'])

            
            for lp in local_ids:
                if lp['exist'] == False: # Delete products which are not avialable in woocommerce
                    WooOrder.objects.filter(order_id=lp['id']).delete()
                
        except DatabaseError as e:
            print('Database error: ' + str(e))

    def sync_customers(self):
        r = self.wcapi.get("customers")
        customers = r.json()

        try:
            local_customer = WooCustomer.objects.values('customer_id')
            
            local_ids = {}
            for lp in local_customer:
                local_ids[lp['customer_id']] = {'exist': False, 'id':lp['customer_id']}

            for WC in customers:
                if local_ids.get(WC['id']) != None: # Exist in both local and woocomerce
                    local_ids[WC['id']]['exist'] = True
                    local_p = WooCustomer.objects.get(customer_id=WC['id'])
                    if (local_p != None) and (WC['date_modified'] != local_p.date_modified):
                        # Updata the local Product

                        local_customerBilling = WooCustomerShipping.objects.get(customer=WC['id'])
                        local_customerShipping = WooCustomerBilling.objects.get(customer=WC['id'])

                        local_p.date_created = WC['date_created']
                        local_p.date_modified = WC['date_modified']
                        local_p.is_paying_customer = WC['is_paying_customer']
                        # meta_data = WC['meta_data'],
                        local_p.customer_id = WC['id']
                        local_p.save()

                        local_customerBilling.first_name = WC['billing']['first_name']
                        local_customerBilling.last_name = WC['billing']['last_name']
                        local_customerBilling.company = WC['billing']['company']
                        local_customerBilling.address_1 = WC['billing']['address_1']
                        local_customerBilling.address_2 = WC['billing']['address_2']
                        local_customerBilling.city = WC['billing']['city']
                        local_customerBilling.state = WC['billing']['state']
                        local_customerBilling.postcode = WC['billing']['postcode']
                        local_customerBilling.country = WC['billing']['country']
                        local_customerBilling.email = WC['billing']['email']
                        local_customerBilling.phone = WC['billing']['phone']
                        local_customerBilling.customer = local_p
                        local_customerBilling.save()

                        local_customerShipping.customer = local_p
                        local_customerShipping.first_name = WC['shipping']['first_name']
                        local_customerShipping.last_name = WC['shipping']['last_name']
                        local_customerShipping.company = WC['shipping']['company']
                        local_customerShipping.address_1 = WC['shipping']['address_1']
                        local_customerShipping.address_2 = WC['shipping']['address_2']
                        local_customerShipping.city = WC['shipping']['city']
                        local_customerShipping.state = WC['shipping']['state']
                        local_customerShipping.postcode = WC['shipping']['postcode']
                        local_customerShipping.country = WC['shipping']['country']
                        local_customerShipping.save()
                        
                else: # Does not exist in local, but exist in woocomerce
                    new_customer = WooCustomer.objects.create(
                        date_created = WC['date_created'],
                        date_modified = WC['date_modified'],
                        is_paying_customer = WC['is_paying_customer'],
                        # meta_data = WC['meta_data'],
                        customer_id = WC['id']
                    )
                    new_customerBilling = WooCustomerBilling.objects.create(
                        first_name = WC['billing']['first_name'],
                        last_name = WC['billing']['last_name'],
                        company = WC['billing']['company'],
                        address_1 = WC['billing']['address_1'],
                        address_2 = WC['billing']['address_2'],
                        city = WC['billing']['city'],
                        state = WC['billing']['state'],
                        postcode = WC['billing']['postcode'],
                        country = WC['billing']['country'],
                        email = WC['billing']['email'],
                        phone = WC['billing']['phone'],
                        customer = new_customer
                    )
                    new_customerShipping = WooCustomerShipping.objects.create(
                        customer = new_customer,
                        first_name = WC['shipping']['first_name'],
                        last_name = WC['shipping']['last_name'],
                        company = WC['shipping']['company'],
                        address_1 = WC['shipping']['address_1'],
                        address_2 = WC['shipping']['address_2'],
                        city = WC['shipping']['city'],
                        state = WC['shipping']['state'],
                        postcode = WC['shipping']['postcode'],
                        country = WC['shipping']['country'],
                    )
            
            for lp in local_ids:
                if lp['exist'] == False: # Delete products which are not avialable in woocommerce
                    WooCustomer.objects.filter(customer_id=lp['id']).delete()
               
        except DatabaseError as e:
            print('Database error: ' + str(e))
