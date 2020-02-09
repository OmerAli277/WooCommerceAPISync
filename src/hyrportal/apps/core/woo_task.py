import json
from woocommerce import API

class woocommerce_api:
    def __init__(self, p_url, p_consumer_key, p_consumer_secret):
        url = p_url
        consumer_key = p_consumer_key
        consumer_secret = p_consumer_secret

    def woo_test(self):
        wcapi = API(
            url="https://automatiseramera.se/",
            consumer_key="ck_092c10db6a942dffe7ce610667e8c42226be7889",
            consumer_secret="cs_0678d389f81fa5060d896e8e5fb50022626bf96b",
            version="wc/v3",
            timeout=30
        )

        r = wcapi.get("products")
        print(r.json())