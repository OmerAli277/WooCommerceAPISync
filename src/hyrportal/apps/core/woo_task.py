import json
import requests
from woocommerce import API
from hyrportal.apps.core.models import User, WooCustomer, WooOrder, WooOrderItem, WooProduct, WooVariant, fortnoxApiDetails
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
        print('omer ')
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
        for p in orders:
            print(p['id'])
            print('\n\n\n\n\n\n\n\n') 

    def sync_customers(self):
        r = self.wcapi.get("customers")
        customers = r.json()
        for p in customers: 
            print(p['id'])
            print('\n\n\n\n\n\n') 
