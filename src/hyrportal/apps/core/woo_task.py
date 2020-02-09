import json
from woocommerce import API

class woocommerce_api:
    def __init__(self, p_url, p_consumer_key, p_consumer_secret):
        self.wcapi = API(
            url = p_url,
            consumer_key = p_consumer_key,
            consumer_secret = p_consumer_secret,
            version = "wc/v3",
            timeout = 30
        )

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