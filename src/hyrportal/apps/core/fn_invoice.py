import json
import requests


class fn_invoice_api:

    def __init__(self, Access_Token, Client_Secret):
        self.Access_Token = Access_Token
        self.Client_Secret = Client_Secret

    def fn_list_of_invoice(self):
        invoices = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/invoices",
                headers = {
                    "Access-Token": self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoices = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_list_of_invoice HTTP Request failed')
        return invoices

    def fn_read_invoice(self, id):
        invoice = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/invoices/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_read_invoice HTTP Request failed') 
        return invoice   

    def fn_create_invoice(self, invoice_json_obj):
        invoice = None
        try:
            r = requests.post(
                url="https://api.fortnox.se/3/invoices",
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Invoice": {
                #         "InvoiceRows": [
                #             {
                #                 "DeliveredQuantity": "10.00",
                #                 "ArticleNumber": "66892"
                #             }
                #         ],
                #         "CustomerNumber": "100"
                #     }
                # }
                data = invoice_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_create_invoice HTTP Request failed')
        return invoice   

    def fn_update_invoice(self, id, invoice_json_obj):
        invoice = None
        try:
            r = requests.put(
                url="https://api.fortnox.se/3/invoices/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Invoice": {
                #         "Freight": "99"
                #     }
                # }
                data = invoice_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            invoice = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_update_invoice HTTP Request failed')
        return invoice   


