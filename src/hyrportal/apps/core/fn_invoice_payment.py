import json
import requests


class fn_invoice_payment_api:

    def __init__(self, Access_Token, Client_Secret):
        self.Access_Token = Access_Token
        self.Client_Secret = Client_Secret

    def fn_list_of_invoice_payment(self):
        invoice_payments = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/invoicepayments",
                headers = {
                    "Access-Token": self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice_payments = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_list_of_invoice_payment HTTP Request failed')
        return invoice_payments

    def fn_read_invoice_payment(self, id):
        invoice_payment = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/invoicepayments/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice_payment = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_read_invoice_payment HTTP Request failed') 
        return invoice_payment   

    def fn_create_invoice_payment(self, invoice_payment_json_obj):
        invoice_payment = None
        try:
            r = requests.post(
                url="https://api.fortnox.se/3/invoicepayments",
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "invoice_payment": {
                #         "invoice_paymentRows": [
                #             {
                #                 "DeliveredQuantity": "10.00",
                #                 "ArticleNumber": "66892"
                #             }
                #         ],
                #         "CustomerNumber": "100"
                #     }
                # }
                data = invoice_payment_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice_payment = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_create_invoice_payment HTTP Request failed')
        return invoice_payment   

    def fn_update_invoice_payment(self, id, invoice_payment_json_obj):
        invoice_payment = None
        try:
            r = requests.put(
                url="https://api.fortnox.se/3/invoicepayments/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "invoice_payment": {
                #         "Freight": "99"
                #     }
                # }
                data = invoice_payment_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice_payment = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_update_invoice_payment HTTP Request failed')
        return invoice_payment   

    def fn_delete_invoice_payment(self, id):
            invoice_payment = None
            try:
                r = requests.delete(
                    url="https://api.fortnox.se/3/invoicepayments/" + id,
                    headers = {
                        "Access-Token":self.Access_Token,
                        "Client-Secret":self.Client_Secret,
                        "Content-Type":"application/json",
                        "Accept":"application/json",
                    }
                )
                print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
                # print('Response HTTP Response Body : {content}'.format(content=r.content))
                invoice_payment = json.loads(r.content)
            except requests.exceptions.RequestException as e:
                print('fn_delete_invoice_payment HTTP Request failed')
            return invoice_payment  
