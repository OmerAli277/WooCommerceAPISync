import requests
import json

class visma_customer_api:

    def __init__(self, client_id):
        self.client_id = client_id

    def visma_authentication(self):
        print("In visma_authentication function")
        user_authentication = None
        try:
            r = requests.get(
                url="https://identity.vismaonline.com/connect/authorize",
                headers = {
                    "client_id"  : self.client_id,
                    "redirect_uri"  : "http://127.0.0.1:8000/callback",
                    "scope"         : "ea:api%20ea:sales",
                    # "Client-Secret" : "01546989oMTQl6OE52h6Oc8b52otWp54203f2Mz25gv4hpNoUt21VK6q72K7xFe",
                    "response_type" : "code"
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            # user_authentication = json.loads(r.content)
            # print("Printing user_authentication" + str(user_authentication))
        except requests.exceptions.RequestException as e:
            print('fn_list_of_customer HTTP Request failed')
        return user_authentication
