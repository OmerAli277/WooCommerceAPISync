import json
import requests
from woocommerce import API
# from .models import User, WooCustomer, WooOrder, WooProduct, WooVariant, fortnoxApiDetails
from hyrportal.apps.core.models import User, WooCustomer, WooOrder, WooOrderItem, WooProduct, WooVariant,\
    fortnoxApiDetails, WooCustomerBilling, WooCustomerShipping
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
        print('omer ali')
        try: 
            local_products = WooProduct.objects.all()
            print(local_products)
            # new_product = WooProduct.objects.create(product_id = '345' , parent_id = '123')
            # new_product.save()
            # local_products = WooProduct.objects.all()
            # print(local_products)


            for lp in local_products:
                print (lp)
                #if lp['product_id'] not in products[]:
                for wp in products:
                    # print(wp['meta_data'])
                    # print('\n\n\n')
                    # if wp['id'] != lp['product_id']:
                    print("I am in!")
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
                    # new_product.save()
                # print (product)

                # elif products


        except DatabaseError as e:
            print('Database error: ' + str(e)) 

        # for p in products:
        #     print(p['id'])
        #     print('\n\n\n\n\n\n\n\n')
    
    def sync_orders(self):
        r = self.wcapi.get("orders")
        orders = r.json()
        print ('In sync_orders')
        try :
            local_orders = WooOrder.objects.all()
            print(local_orders)
            for WO in orders:
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

                # new_order.save()
        except DatabaseError as e:
            print('Database error: ' + str(e))

        # for order in local_orders:
        #     print(order['id'])
        #     for WO in orders:
        #         new_order = WooOrder.objects.create(
        #         order_id = WO['id'],
        #         parent_id = WO['parent_id'],
        #         number = WO['number'],
        #         order_key =  WO['order_key'],
        #         created_via =  WO['created_via'],
        #         version =  WO['version'],
        #         status =  WO['status'],
        #         currency =  WO['currency'],
        #         discount_total = WO['discount_total'],
        #         discount_tax =  WO['discount_tax'],
        #         shipping_total =  WO['shipping_total'],
        #         shipping_tax =  WO['shipping_tax'],
        #         cart_tax =  WO['cart_tax'],
        #         total =  WO['total'],
        #         total_tax =  WO['total_tax'],
        #         prices_include_tax =  WO['prices_include_tax'],
        #         payment_method =  WO['payment_method'],
        #         payment_method_title = WO['payment_method_title'],
        #         transaction_id =  WO['transaction_id'],
        #
        #         date_created = WO['date_created'],
        #         date_modified = WO['date_modified'],
        #         date_paid = WO['date_paid'],
        #         date_completed = WO['date_completed'])


        # for p in orders:
        #     print(p['id'])
            # print('\n\n\n\n\n\n\n\n')

    def sync_customers(self):
        r = self.wcapi.get("customers")
        customers = r.json()
        try:
            for WC in customers:
                new_customer = WooCustomer.objects.create(
                    date_created = WC['date_created'],
                    date_modified = WC['date_modified'],
                    is_paying_customer = WC['is_paying_customer'],
                    # meta_data = WC['meta_data'],
                    customer_id = WC['id']
                )
                new_customer.save()
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
        except DatabaseError as e:
            print('Database error: ' + str(e))
        # for p in customers:
            # print(p['id'])
            # print('\n\n\n\n\n\n')
