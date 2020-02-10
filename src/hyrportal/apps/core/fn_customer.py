import json
import requests


class fn_customer_api:

    def __init__(self, Access_Token, Client_Secret):
        self.Access_Token = Access_Token
        self.Client_Secret = Client_Secret

    def fn_list_of_customer(self):
        customers = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/customers",
                headers = {
                    "Access-Token": self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            customers = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_list_of_customer HTTP Request failed')
        return customers

    def fn_read_customer(self, id):
        customer = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/customers/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            customer = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_read_customer HTTP Request failed') 
        return customer   

    def fn_create_customer(self, customer_json_obj):
        customer = None
        try:
            r = requests.post(
                url="https://api.fortnox.se/3/customers",
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Customer": {
                #         "Name": "Klara Norström"
                #     }
                # }
                data = customer_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            customer = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_create_customer HTTP Request failed')
        return customer   

    def fn_update_customer(self, id, customer_json_obj):
        customer = None
        try:
            r = requests.put(
                url="https://api.fortnox.se/3/customers/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Customer": {
                #         "Address1": "Hällesjö",
                #         "City": "Hultsfred",
                #         "CountryCode": "SE",
                #         "ZipCode": "57737"
                #     }
                # }
                data = customer_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            customer = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_update_customer HTTP Request failed')
        return customer   

    def fn_delete_customer(self, id):
        customer = None
        try:
            r = requests.delete(
                url="https://api.fortnox.se/3/customers/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            customer = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_delete_customer HTTP Request failed')
        return customer   

