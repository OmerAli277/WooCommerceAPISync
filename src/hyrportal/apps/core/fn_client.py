import json
import requests


class fn_article_api:
    def __init__(self, Access_Token, Client_Secret):
        self.Access_Token = Access_Token
        self.Client_Secret = Client_Secret
        
    def fn_list_of_article(self):
        articles = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/articles",
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            articles = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_list_of_article HTTP Request failed')
        return articles

    def fn_read_article(self, id):
        article = None
        try:
            r = requests.get(
                url="https://api.fortnox.se/3/articles/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            article = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_read_article HTTP Request failed')   
        return article

    def fn_create_article(self, article_json_obj):
        article = None
        try:
            r = requests.post(
                url="https://api.fortnox.se/3/articles",
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Article": {
                #         "Description": "Extra förpackning",
                #         "ArticleNumber": "FRPPLUS"
                #     }
                # }
                data = article_json_obj
                )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            article = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_create_article HTTP Request failed')
        return article

    def fn_update_article(self, id, article_json_obj):
        article = None
        try:
            r = requests.put(
                url="https://api.fortnox.se/3/articles/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
                # data = json.dumps({
                #     "Article": {
                #         "Unit": "st",
                #         "ArticleNumber": "FRPPLUS"
                #     }
                # }
                data = article_json_obj
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            article = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_update_article HTTP Request failed')
        return article

    def fn_delete_article(self, id):
        article = None
        try:
            r = requests.delete(
                url="https://api.fortnox.se/3/articles/" + id,
                headers = {
                    "Access-Token":self.Access_Token,
                    "Client-Secret":self.Client_Secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            # print('Response HTTP Response Body : {content}'.format(content=r.content))
            article = json.loads(r.content)
        except requests.exceptions.RequestException as e:
            print('fn_delete_article HTTP Request failed')
        return article


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


