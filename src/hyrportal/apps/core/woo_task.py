import json
import requests
from woocommerce import API
# from .models import User, WooCustomer, WooOrder, WooProduct, WooVariant, fortnoxApiDetails, WooCustomerShipping, WooCustomerBilling
from hyrportal.apps.core.models import User, WooCustomer, WooOrder, WooOrderItem, WooProduct, WooVariant, WooCustomerShipping, WooCustomerBilling ,fortnoxApiDetails
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
    
    # Article
    def fn_article_obj(self, WP):

        if WP['short_description'] != "":
            WP['short_description'] = "Kindly provide description."

        fn_article_object = {
            "Article": {
                # "@url": "https://api.fortnox.se/3/articles/FRPPLUS",
                "ArticleNumber": WP['id'],
                "Description": WP['short_description'],
                "EAN": "",
                "EUAccount": eu_sales_account,  
                "EUVATAccount": eu_vat_account,
                "ExportAccount": non_eu_account,
                "Height": WP['dimensions']['height'],
                # "Housework": false,
                # "HouseworkType": null,
                # "Manufacturer": null,
                # "ManufacturerArticleNumber": "",
                "Note": WP['description'],
                # "PurchaseAccount": purchase_account,
                # "PurchasePrice": 0,
                "QuantityInStock": WP['stock_quantity'],
                # "ReservedQuantity": 0,
                # "SalesAccount": sales_account,
                # "StockGoods": false,
                # "StockPlace": null,
                # "StockValue": 0,
                # "StockWarning": 0,
                # "SupplierName": null,
                # "SupplierNumber": null,
                "Type": WP['type'],
                # "Unit": null,
                # "VAT": vat_rate,
                "WebshopArticle": true,
                "Weight": WP['weight'],
                "Width": WP['dimensions']['width'],
                "SalesPrice": WP['sale_price'],
            }
        }

        return json.dumps(fn_article_object)

    def fn_article_obj_u(self, WP):

        if WP['short_description'] != "":
            WP['short_description'] = "Kindly provide description."

        fn_article_object = {
            "Article": {
                # "@url": "https://api.fortnox.se/3/articles/FRPPLUS",
                # "Active": true,
                "ArticleNumber": WP['id'],
                "Description": WP['short_description'],
                #"EAN": "",
                "EUAccount": eu_sales_account,  
                "EUVATAccount": eu_vat_account,
                "ExportAccount": non_eu_account,
                "Height": WP['dimensions']['height'],
                "Height": WP['dimensions']['height'],
                # "Housework": false,
                # "HouseworkType": null,
                # "Manufacturer": null,
                # "ManufacturerArticleNumber": "",
                "Note": WP['description'],
                # "PurchaseAccount": purchase_account,
                # "PurchasePrice": 0,
                "QuantityInStock": WP['stock_quantity'],
                # "ReservedQuantity": 0,
                # "SalesAccount": sales_account,
                # "StockGoods": false,
                # "StockPlace": null,
                # "StockValue": 0,
                # "SupplierName": null,
                # "SupplierNumber": null,
                "Type": WP['type'],
                # "VAT": vat_rate,
                "WebshopArticle": true,
                "Weight": WP['weight'],
                "Width": WP['dimensions']['width'],
                "SalesPrice": WP['sale_price'],
               
            }
        }

        customer = json.dumps(fn_article_object)
        return customer
    
    def sync_products(self):

         # client_secret, access_token = self.fortnox_authentication()

        client_secret = 'Pmw91MFrEm' 
        access_token = 'c40acba2-3eb9-4d84-9bea-497ea5959542'

        fn_article = fn_article_api(access_token, client_secret)


        r = self.wcapi.get("products")
        products = r.json()
        
        try:
            local_products = WooProduct.objects.values('product_id')

            local_ids = {}
            for lp in local_products:
                local_ids[lp['product_id']] = {'exist': False, 'id':lp['product_id']}

            for wp in products:
                if local_ids.get(wp['id']) != None: # Exist in both local and woocomerce
                    local_ids[wp['id']]['exist'] = True
                    local_p = WooProduct.objects.get(product_id=wp['id'])
                    if (local_p != None) and (wp['date_modified'] != local_p.date_modified):
                        # Updata the local Product
                        local_p.product_id = wp['id'] 
                        local_p.parent_id = wp['parent_id']
                        local_p.name = wp['name']
                        local_p.slug = wp['slug'] 
                        local_p.permalink = wp['permalink'] 
                        local_p.description = wp['description'] 
                        local_p.short_description = wp['short_description'] 
                        local_p.sku = wp['sku']
                        local_p.type = wp['type'] 
                        local_p.price_html  = wp['price_html']  
                        local_p.status = wp['status']
                        local_p.catalog_visibility = wp['catalog_visibility'] 
                        local_p.stock_quantity = wp['stock_quantity']
                        local_p.stock_status = wp['stock_status']
                        local_p.tax_status = wp['tax_status']
                        local_p.tax_class = wp['tax_class']
                        local_p.shipping_class = wp['shipping_class'] 
                        local_p.shipping_class_id = wp['shipping_class_id'] 
                        local_p.backorders = wp['backorders']

                        local_p.price = wp['price']
                        local_p.regular_price = wp['regular_price']
                        local_p.sale_price = wp['sale_price']
                        local_p.total_sales = wp['total_sales'] 
                        
                        local_p.featured = wp['featured']
                        local_p.on_sale = wp['on_sale']
                        local_p.purchasable = wp['purchasable'] 
                        local_p.virtual =wp['virtual']
                        local_p.downloadable =wp['downloadable']  
                        local_p.manage_stock = wp['manage_stock'] 
                        local_p.backorders_allowed= wp['backorders_allowed']
                        local_p.backordered = wp['backordered']
                        local_p.sold_individually = wp['sold_individually'] 
                        local_p.shipping_required = wp['shipping_required']
                        local_p.save()

                        # fortnox API Update
                        result = fn_article.fn_update_article(str(wp['id']), self.fn_article_obj_u(wp))
                        print('Arctile Updated:')
                        print(result)

                else: # Does not exist in local, but exist in woocomerce
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
                        shipping_required = wp['shipping_required'],
                        # shipping_taxable= wp['shipping_taxable']
                        # meta_data = wp['meta_data'], 
                        date_created = wp['date_created']
                        )
                    
                    # Fortnox API Create
                    result = fn_article.fn_create_article(self.fn_article_obj(wp))
                    print('Article created:')
                    print(result)


            for lp in local_ids:
                if local_ids[lp]['exist'] == False: # Delete products which are not avialable in woocommerce
                    WooProduct.objects.filter(product_id=local_ids[lp]['id']).delete()

                    # Fortnox API Create
                    result = fn_article.fn_delete_article(str(local_ids[lp]['id']))
                    print('Article created:')
                    print(result)

        except DatabaseError as e:
            print('Database error: ' + str(e)) 
    

    # Order and Fortnox Invoice

    def fn_invoice_obj(self, WO):

        row_items = []
        for item in  WO['line_items']:
            row_items.push({
                {
                    "AccountNumber": sales_account,
                    "ArticleNumber": item['product_id'],
                    "DeliveredQuantity": item['quantity'],
                    "Description": "USB-minne 32GB",
                    # "Discount": 0,
                    # "DiscountType": "PERCENT",
                    # "HouseWork": false,
                    # "HouseWorkHoursToReport": null,
                    # "HouseWorkType": null,
                    "Price": item['price'],
                    # "Project": 0,
                    "Total": item['total'],
                    # "Unit": "st",
                     "VAT": vat_rate,
                }
            })


        fn_invoice = {
            "Invoice": {
                # "@url": "https://api.fortnox.se/3/invoices/204",
                # "@urlTaxReductionList": "https://api.fortnox.se/3/taxreductions?filter=invoices&referencenumber=204",
                "Address1": WO['billing']['address_1'],
                "Address2": WO['billing']['address_2'],
                "City": WO['billing']['city'],
                "Comments": "",
                "Country": WO['billing']['country'],
                # "Credit": "false",  if amount is negative, value is true
                "Currency": WO['currency'],
                # "CurrencyRate": 1,
                # "CurrencyUnit": 1,
                "CustomerName": WO['billing']['first_name'] + WO['Billing']['last_name'],
                "CustomerNumber": WO['customer_id'],
                "DeliveryAddress1": WO['shipping']['address_1'],
                "DeliveryAddress2": WO['shipping']['address_2'],
                "DeliveryCity": WO['shipping']['city'],
                "DeliveryCountry": WO['shipping']['country'],
                "DeliveryZipCode": WO['shipping']['postcode'],
                "DocumentNumber": WO['id'],
                "ExternalInvoiceReference1": "",
                "ExternalInvoiceReference2": "",
                "Freight": "",
                "InvoiceDate": WO['date_created'],
                "InvoiceRows": row_items,
                "InvoiceType": "INVOICE",
                # "Labels": [
                #     {
                #         "Id": 5
                #     },
                #     {
                #         "Id": 11
                #     }
                # ],
                # "Net": 1590,
                # "OrderReference": 0,
                # "OrganisationNumber": "",
                # "OurReference": "",
                "Phone1": WO['billing']['phone'],
                # "Project": 0,
                # "TermsOfPayment": "30",
                "Total": WO['total'],
                # "TotalToPay": 1988,
                # "TotalVAT": 397.5,
                # "VATIncluded": false,
                "YourOrderNumber": WO['id'],
            }
        }

        return json.dumps(fn_invoice)
    
    def fn_invoice_obj_u(self, WO):

        row_items = []
        for item in  WO['line_items']:
            row_items.push({
                {
                    "AccountNumber": sales_account,
                    "ArticleNumber": item['product_id'],
                    "DeliveredQuantity": item['quantity'],
                    # "Description": "USB-minne 32GB",
                    # "Discount": 0,
                    # "DiscountType": "PERCENT",
                    # "HouseWork": false,
                    # "HouseWorkHoursToReport": null,
                    # "HouseWorkType": null,
                    "Price": item['price'],
                    # "Project": 0,
                    "Total": item['total'],
                    # "Unit": "st",
                    # "VAT": 25
                }
            })


        fn_invoice = {
            "Invoice": {
                # "@url": "https://api.fortnox.se/3/invoices/204",
                # "@urlTaxReductionList": "https://api.fortnox.se/3/taxreductions?filter=invoices&referencenumber=204",
                "Address1": WO['billing']['address_1'],
                "Address2": WO['billing']['address_2'],
                "Balance": 1988,
                "Cancelled": False,
                "City": WO['billing']['city'],
                # "Comments": "",
                # "CostCenter": "",
                "Country": WO['billing']['country'],
                # "Credit": "false",
                "Currency": WO['currency'],
                # "CurrencyRate": 1,
                # "CurrencyUnit": 1,
                "CustomerName": WO['billing']['first_name'] + WO['Billing']['last_name'],
                "CustomerNumber": WO['customer_id'],
                "DeliveryAddress1": WO['shipping']['address_1'],
                "DeliveryAddress2": WO['shipping']['address_2'],
                "DeliveryCity": WO['shipping']['city'],
                "DeliveryCountry": WO['shipping']['country'],
                # "DeliveryDate": null,
                # "DeliveryName": "",
                "DeliveryZipCode": WO['shipping']['postcode'],
                # "ExternalInvoiceReference1": "",
                # "ExternalInvoiceReference2": "",
                # "Freight": "0,00",
                # "HouseWork": false,
                "InvoiceDate": WO['date_created'],
                "InvoiceRows": row_items,
                "InvoiceType": "INVOICE",
                # "Net": 1590,
                # "OrderReference": 0,
                # "OrganisationNumber": "",
                # "OurReference": "",
                "Phone1": WO['billing']['phone'],
                # "Project": 0,
                # "TermsOfPayment": "30",
                "Total": WO['total'],
                # "VATIncluded": false,
            }
        }

        return json.dumps(fn_invoice)
    
    def fn_invoice_payment_obj(self, WO):

        fn_invoice_payment = {
            "InvoicePayment": {
                # "@url": "https://api.fortnox.se/3/invoicepayments/1",
                "Amount": WO['total'],
                "AmountCurrency": WO['total'],
                "Currency": WO['currency'],
                # "CurrencyRate": 1,
                # "CurrencyUnit": 1,
                # "ExternalInvoiceReference2": "",
                "InvoiceCustomerName": WO['billing']['first_name'] + WO['billing']['last_name'],
                "InvoiceCustomerNumber": WO['customer_id'],
                "InvoiceNumber": WO['id'],
                "InvoiceTotal": WO['total'],
                # "ModeOfPayment": WO['payment_method'],
                 "ModeOfPaymentAccount": payout_account,
                # "Number": "2",
                "PaymentDate": WO['date_paid'],
                # "WriteOffs": []
            }
        }

        return json.dumps(fn_invoice_payment)

    def fn_invoice_payment_obj_u(self, WO):

        fn_invoice_payment = {
            "InvoicePayment": {
                # "@url": "https://api.fortnox.se/3/invoicepayments/1",
                "Amount": WO['total'],
                "AmountCurrency": WO['total'],
                "Currency": WO['currency'],
                # "CurrencyRate": 1,
                # "CurrencyUnit": 1,
                "InvoiceCustomerName": WO['billing']['first_name'] + WO['billing']['last_name'],
                "InvoiceCustomerNumber": WO['customer_id'],
                "InvoiceNumber": "", #fortnox invoice numer
                "InvoiceTotal": WO['total'],
                # "ModeOfPayment": WO['payment_method'],
                "ModeOfPaymentAccount": payout_account,
                # "Number": "2",
                "PaymentDate": WO['date_paid'],
                # "WriteOffs": []
            }
        }

        return json.dumps(fn_invoice_payment)

    def sync_orders(self):
        # client_secret, access_token = self.fortnox_authentication()

        client_secret = 'Pmw91MFrEm' 
        access_token = 'c40acba2-3eb9-4d84-9bea-497ea5959542'

        fn_invoice = fn_invoice_api(access_token, client_secret)
        fn_invoice_payment = fn_invoice_payment_api(access_token, client_secret)


        r = self.wcapi.get("orders")
        orders = r.json()
        print ('In sync_orders')
        try :
            local_orders = WooOrder.objects.values('order_id')
            print(local_orders)

            local_ids = {}
            for lp in local_orders:
                local_ids[lp['order_id']] = {'exist': False, 'id':lp['order_id']}

            for WO in orders:
                if local_ids.get(WO['id']) != None: # Exist in both local and woocomerce
                    local_ids[WO['id']]['exist'] = True
                    local_p = WooOrder.objects.get(order_id=WO['id'])
                    if (local_p != None) and (WO['date_modified'] != local_p.date_modified):
                        # Updata the local Product
                        local_p.order_id = WO['id']
                        local_p.parent_id = WO['parent_id']
                        local_p.number = WO['number']
                        local_p.order_key =  WO['order_key']
                        local_p.created_via =  WO['created_via']
                        local_p.version =  WO['version']
                        local_p.status =  WO['status']
                        local_p.currency =  WO['currency']
                        local_p.discount_total = WO['discount_total']
                        local_p.discount_tax =  WO['discount_tax']
                        local_p.shipping_total =  WO['shipping_total']
                        local_p.shipping_tax =  WO['shipping_tax']
                        local_p.cart_tax =  WO['cart_tax']
                        local_p.total =  WO['total']
                        local_p.total_tax =  WO['total_tax']
                        local_p.prices_include_tax =  WO['prices_include_tax']
                        local_p.payment_method =  WO['payment_method']
                        local_p.payment_method_title = WO['payment_method_title']
                        local_p.transaction_id =  WO['transaction_id']

                        local_p.date_modified = WO['date_modified']
                        local_p.date_paid = WO['date_paid']
                        local_p.date_completed = WO['date_completed']

                        local_p.save()

                        # Fortnox API Update
                        if WO['status'] != "completed" : 
                            result  = fn_invoice.fn_update_invoice(WO['id'], self.fn_invoice_obj_u(WO))
                            print('Invoice Updated:')
                            print(result)
                        else:
                            result  = fn_invoice_payment.fn_update_invoice_payment(WO['id'], self.fn_invoice_payment_obj_u(WO))
                            print('Invoice payment Updated:')
                            print(result)

                    else: # Does not exist in local, but exist in woocomerce
                     new_order = WooOrder.objects.create(
                        order_id = WO['id'],
                        parent_id = WO['parent_id'],
                        number = WO['number'],
                        order_key =  WO['order_key'],
                        created_via =  WO['created_via'],
                        version =  WO['version'],
                        status =  WO['status'],
                        currency =  WO['currency'],
                        discount_total = WO['discount_total'],
                        discount_tax =  WO['discount_tax'],
                        shipping_total =  WO['shipping_total'],
                        shipping_tax =  WO['shipping_tax'],
                        cart_tax =  WO['cart_tax'],
                        total =  WO['total'],
                        total_tax =  WO['total_tax'],
                        prices_include_tax =  WO['prices_include_tax'],
                        payment_method =  WO['payment_method'],
                        payment_method_title = WO['payment_method_title'],
                        transaction_id =  WO['transaction_id'],

                        date_created = WO['date_created'],
                        date_modified = WO['date_modified'],
                        date_paid = WO['date_paid'],
                        date_completed = WO['date_completed'])

                    # Fortnox API Update
                    if WO['status'] != "completed" :
                        result  = fn_invoice.fn_create_invoice(self.fn_invoice_obj(WO))
                        print('Invoice created:')
                        print(result)
                    else:
                        result  = fn_invoice_payment.fn_create_invoice_payment(self.fn_invoice_obj(WO))
                        print('Invoice payment created:')
                        print(result)
            
            for lp in local_ids:
                if local_ids[lp]['exist'] == False: # Delete products which are not avialable in woocommerce
                    result = WooOrder.objects.get(order_id=local_ids[lp]['id'])
                    
                    # result1 = fn_invoice.fn
                    # # fotnox delete
                    # if result.status == 'complete' :

                    WooOrder.objects.filter(order_id=local_ids[lp]['id']).delete()


                
        except DatabaseError as e:
            print('Database error: ' + str(e))


    # Customer 
    def fn_customer_obj(self, WC):

        fn_name = WC['billing']['first_name'] + WC['billing']['last_name']

        fn_customer_object = {
            "Customer": {
                "Address1": WC['billing']['address_1'],
                "Address2": WC['billing']['address_2'],
                "City": WC['billing']['city'],
                "Country": WC['billing']['country'],
                "CountryCode": WC['billing']['postcode'],
                "Currency": "SEK",
                "CustomerNumber": WC['id'],
                "DeliveryAddress1": WC['shipping']['address_1'],
                "DeliveryAddress2": WC['shipping']['address_2'],
                "DeliveryCity": WC['shipping']['city'],
                "DeliveryCountry": WC['shipping']['country'],
                "DeliveryCountryCode": WC['shipping']['postcode'],
                "DeliveryName": WC['billing']['first_name'],
                "DeliveryPhone1": WC['billing']['phone'],
                "Email": WC['billing']['email'],
                "Name": fn_name,
                "OrganisationNumber": "company_vat_id",
            }
        }
        
        fn_customer_object = json.dumps(fn_customer_object)

        return fn_customer_object

    def fn_customer_obj_u(self, WC):

        fn_name = WC['billing']['first_name'] + WC['billing']['last_name']

        fn_customer_object = {
            "Customer": {
                "Address1": WC['billing']['address_1'],
                "Address2": WC['billing']['address_2'],
                "City": WC['billing']['city'],
                "Country": WC['billing']['country'],
                "CountryCode": WC['billing']['postcode'],
                "Currency": "SEK",
                # "CustomerNumber": WC['id'],
                "DeliveryAddress1": WC['shipping']['address_1'],
                "DeliveryAddress2": WC['shipping']['address_2'],
                "DeliveryCity": WC['shipping']['city'],
                "DeliveryCountry": WC['shipping']['country'],
                "DeliveryCountryCode": WC['shipping']['postcode'],
                "DeliveryName": WC['billing']['first_name'],
                "DeliveryPhone1": WC['billing']['phone'],
                "Email": WC['billing']['email'],
                "Name": fn_name,
                "OrganisationNumber": "company_vat_id",
            }
        }
        
        fn_customer_object = json.dumps(fn_customer_object)

        return fn_customer_object

    def sync_customers(self):
        # client_secret, access_token = self.fortnox_authentication()

        client_secret = 'Pmw91MFrEm' 
        access_token = 'c40acba2-3eb9-4d84-9bea-497ea5959542'

        fn_customer = fn_customer_api(access_token, client_secret)

        r = self.wcapi.get("customers")
        customers = r.json()

        try:
            local_customer = WooCustomer.objects.values('customer_id')
            
            local_ids = {}
            for lp in local_customer:
                local_ids[lp['customer_id']] = {'exist': False, 'id':lp['customer_id']}

            for WC in customers:
                if local_ids.get(WC['id']) != None: # Exist in both local and woocomerce
                    local_ids[WC['id']]['exist'] = True
                    local_p = WooCustomer.objects.get(customer_id=WC['id'])
                    if (local_p != None) and (WC['date_modified'] != local_p.date_modified):
                        # Updata the local Product

                        local_customerBilling = WooCustomerShipping.objects.get(customer=WC['id'])
                        local_customerShipping = WooCustomerBilling.objects.get(customer=WC['id'])

                        local_p.date_created = WC['date_created']
                        local_p.date_modified = WC['date_modified']
                        local_p.is_paying_customer = WC['is_paying_customer']
                        # meta_data = WC['meta_data'],
                        local_p.customer_id = WC['id']
                        local_p.first_name = WC['first_name']
                        local_p.last_name = WC['last_name']
                        local_p.username = WC['username']
                        local_p.email = WC['email']
                        local_p.save()

                        local_customerBilling.first_name = WC['billing']['first_name']
                        local_customerBilling.last_name = WC['billing']['last_name']
                        local_customerBilling.company = WC['billing']['company']
                        local_customerBilling.address_1 = WC['billing']['address_1']
                        local_customerBilling.address_2 = WC['billing']['address_2']
                        local_customerBilling.city = WC['billing']['city']
                        local_customerBilling.state = WC['billing']['state']
                        local_customerBilling.postcode = WC['billing']['postcode']
                        local_customerBilling.country = WC['billing']['country']
                        local_customerBilling.email = WC['billing']['email']
                        local_customerBilling.phone = WC['billing']['phone']
                        local_customerBilling.customer = local_p
                        local_customerBilling.save()

                        local_customerShipping.customer = local_p
                        local_customerShipping.first_name = WC['shipping']['first_name']
                        local_customerShipping.last_name = WC['shipping']['last_name']
                        local_customerShipping.company = WC['shipping']['company']
                        local_customerShipping.address_1 = WC['shipping']['address_1']
                        local_customerShipping.address_2 = WC['shipping']['address_2']
                        local_customerShipping.city = WC['shipping']['city']
                        local_customerShipping.state = WC['shipping']['state']
                        local_customerShipping.postcode = WC['shipping']['postcode']
                        local_customerShipping.country = WC['shipping']['country']
                        local_customerShipping.save()

                        #fortnox API Update
                        fn_result = fn_customer.fn_update_customer(str(WC['id']) , self.fn_customer_obj_u(WC))
                        print('Customer Update:')
                        print(fn_result)

                        
                else: # Does not exist in local, but exist in woocomerce
                    new_customer = WooCustomer.objects.create(
                        date_created = WC['date_created'],
                        date_modified = WC['date_modified'],
                        is_paying_customer = WC['is_paying_customer'],
                        # meta_data = WC['meta_data'],
                        customer_id = WC['id']
                    )
                    new_customerBilling = WooCustomerBilling.objects.create(
                        first_name = WC['billing']['first_name'],
                        last_name = WC['billing']['last_name'],
                        company = WC['billing']['company'],
                        address_1 = WC['billing']['address_1'],
                        address_2 = WC['billing']['address_2'],
                        city = WC['billing']['city'],
                        state = WC['billing']['state'],
                        postcode = WC['billing']['postcode'],
                        country = WC['billing']['country'],
                        email = WC['billing']['email'],
                        phone = WC['billing']['phone'],
                        customer = new_customer
                    )
                    new_customerShipping = WooCustomerShipping.objects.create(
                        customer = new_customer,
                        first_name = WC['shipping']['first_name'],
                        last_name = WC['shipping']['last_name'],
                        company = WC['shipping']['company'],
                        address_1 = WC['shipping']['address_1'],
                        address_2 = WC['shipping']['address_2'],
                        city = WC['shipping']['city'],
                        state = WC['shipping']['state'],
                        postcode = WC['shipping']['postcode'],
                        country = WC['shipping']['country'],
                    )

                    # Fortnox API Create
                    fn_result = fn_customer.fn_create_customer(self.fn_customer_obj(WC))
                    print('Customer Created:')
                    print(fn_result)
            
            for lp in local_ids:
                if local_ids[lp]['exist'] == False: # Delete products which are not available in WooCommerce
                    WooCustomer.objects.filter(customer_id=local_ids[lp]['id']).delete()

                    # Fortnox API Delete
                    fn_result = fn_customer.fn_delete_customer(str(local_ids[lp]['id']))
                    print('Customer Update:')
                    print(fn_result)
               
        except DatabaseError as e:
            print('Database error: ' + str(e))
