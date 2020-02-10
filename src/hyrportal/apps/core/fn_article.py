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
