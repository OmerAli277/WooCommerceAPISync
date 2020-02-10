import json
import requests
from woocommerce import API
from hyrportal.apps.core.models import User, WooCustomer, WooOrder, WooOrderItem, WooProduct, WooVariant, fortnoxApiDetails
from .fn_article import fn_article_api
from .fn_customer import fn_customer_api

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
        for p in products:
            print(p['id'])
            print('\n\n\n\n\n\n\n\n') 
    
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