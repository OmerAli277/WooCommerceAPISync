from django.contrib.auth import logout, hashers, login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
import requests
from django.template import RequestContext
from hyrportal import settings

from hyrportal.apps.core.visma_client import visma_customer_api
from hyrportal.apps.core.woo_task import woo_fn_sync
from .models import WooCustomer, WooOrder, WooProduct, User, fortnoxApiDetails , fortnoxSettings , WooCommerceDetails
import json
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, RedirectView
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from .woo_task import woocommerce_api
# from rest_framework import generics, permissions
# from rest_framework.views import APIView
# from .serializers import UserSerialzer, CustomerSerialzer, ProductSerialzer, OrderSerialzer
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Tokens
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin

# from .woo_task import woo_fn_sync


# wp = woo_fn_sync("https://automatiseramera.se/", "ck_092c10db6a942dffe7ce610667e8c42226be7889", "cs_0678d389f81fa5060d896e8e5fb50022626bf96b")

# wp.sync_products()
# wp.sync_customers()
# wp.sync_orders()


#Display connect page to the customer
@login_required()
def connect(request):
    if request.user.is_superuser is False:
        basetemplate = 'auth1.html'
    else:
        basetemplate = 'auth.html'

    return render(request, 'customer/connect.html' , {'template_base' : basetemplate })


def callback(request):
    client_id = "hyr1"
    # print("In visma_authentication function")
    # user_authentication = None
    # try:
    #     r = requests.get(
    #         url="https://identity.vismaonline.com/connect/authorize",
    #         headers = {
    #             "Access-Token"  : client_id,
    #             "redirect_uri"  : "http://127.0.0.1:8000/callback",
    #             "scope"         : "ea:api%20ea:sales",
    #             "response_type" : "code"
    #         },
    #     )
    #     print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
    #     # print('Response HTTP Response Body : {content}'.format(content=r.content))
    #     user_authentication = json.loads(r.content)
    #     print("Printing user_authentication" + str(user_authentication))
    # except requests.exceptions.RequestException as e:
    #     print('fn_list_of_customer HTTP Request failed')
    # return user_authentication

    print("In callback function")
    visma = visma_customer_api(client_id)
    visma.visma_authentication()


    return render(request, 'registration/signup.html')

#handles the request for Logging in of customer or superuser
def request(request):
    if request.method == 'POST':
        email = request.POST.get('InputEmail1')
        password = request.POST.get('InputPassword')
        user = authenticate(request, username = email, password= password)
        if user is not None:
            auth.login(request, user)
            request.session['is_login'] = 'true'
            return redirect('/')
        else:
            return render(request, '401.html')
    else:
        return render(request, '401.html')

#this view is called when super user wants to add a new customer by clicking ADD USER from portal
@user_passes_test(lambda u: u.is_superuser)
def signup(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            companyName = request.POST.get('Company_Name')
            comapanyVat = request.POST.get('Company_Vat')
            user_name = request.POST.get('User_Name')
            customerNum = request.POST.get('Customer_Number')
            # accountType = request.POST.get('account_type')
            email = request.POST.get('inputEmail')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            Address = request.POST.get('inputAddress')
            city = request.POST.get('inputCity')
            zipCode = request.POST.get('inputZip')
            BoxChecked = request.POST.get('gridCheck')
            CustomerName = request.POST.get('CustomerName')

            if password2 == password1:
                user = User.objects.create_user(username=user_name,
                                                email=email,
                                                password=password1,
                                                company_name=companyName,
                                                address=Address,
                                                city=city,
                                                zip_code=zipCode,
                                                customer_name = CustomerName,
                                                customer_no=customerNum ,
                                                company_vat = comapanyVat,
                                                is_seller=True)

                fortnox_Settings = fortnoxSettings.objects.create(
                                                                seller_id = user,
                                                                start_date = None,
                                                                sales_account_25 = 0,
                                                                sales_account_12  = 0,
                                                                sales_account_6  = 0,
                                                                freight_account = "Null" )
                user.save()
                return redirect('/')
            else:
                message = 'Password not matched!'
                return render(request, 'registration/signup.html', {'message' : message})
        else:
            return render(request, 'registration/signup.html')

    else:
        html = "<html><body>Access Denied.%s.</body></html>"
        return HttpResponse(html)

#this is a logout view
class LogoutView(View):
    def get(self, request,  *args, **kwargs):
        del request.session['is_login']
        logout(request)
        return redirect('/')

#Render and homepage(settings) page and authenticate either a user is a customer or a super user
def home_page(request):
    is_login = request.session.get('is_login' , 'false')
    if is_login == 'false':
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.user.is_superuser:
            try:
                fortnoxSettings.objects.get(seller_id = request.user)
            except:
                fortnox_Settings = fortnoxSettings.objects.create(
                                                                seller_id = request.user,
                                                                start_date = None,
                                                                sales_account_25 = 0,
                                                                sales_account_12  = 0,
                                                                sales_account_6  = 0,
                                                                freight_account = "Null" )
            return redirect('settings')
        else:
            return redirect('customer-settings')



#Display the data of the current user currently loged in
# @login_required()
class FortnoxSettingView(UpdateView):
    print("IN FortnoxSettingView")
    template_name = 'customer/connect.html'
    model = fortnoxSettings
    template_base_user = 'auth1.html'
    template_base_superuser = 'auth.html'
    fields = [
        "start_date",
        "sales_account_25",
        "sales_account_12",
        "sales_account_6",
        "freight_account"
    ]
    success_url = reverse_lazy('connect')

    # def get_context_data(self, **context):
    #     context = locals()
    #     if self.request.user.is_superuser is False:
    #         context['template_base'] = self.template_base_user
    #     else:
    #         context['template_base'] = self.template_base_superuser
    #     return context

    def get_object(self, *args, **kwargs):
        return self.model.objects.get(seller_id = self.request.user)

class CustomerSettingsView(UpdateView):
    template_name = 'customer/settings.html'
    model = User
    fields = [
        'customer_name',
        'company_name',
        'address',
        'company_vat',
        'zip_code',
        'city',
        'customer_no'
    ]

    success_url = reverse_lazy('customer-settings')

    def get_object(self, *args, **kwargs):
        return self.request.user

#Decorator to check if the user is completing requirements for a certian action
def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

#Display the data of the current super user currently loged in
@superuser_required()
class SettingsView(UpdateView):
    template_name = 'settings.html'
    model = User
    fields = [
        'customer_name',
        'company_name',
        'address',
        'company_vat',
        'zip_code',
        'customer_no',
        'city'
    ]

    success_url = reverse_lazy('settings')

    def get_object(self, *args, **kwargs):
        return self.request.user

#Display the list of the customer in the current system
@superuser_required()
class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user/list.html'
    model = User

    def get_context_data(self, **kwargs):
        sellers = list(User.objects.all().filter(is_seller=True))
        return dict(
            sellers=[
                dict(
                    id=s.id,
                    customer_no=s.customer_no,
                    customer_name=s.customer_name,
                    account_type=s.account_type,
                )
                for s in sellers
            ]
        )

#Allow the super user to Update the data of the customer selected
@superuser_required()
class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'user/edit.html'
    model = User
    fields = [
        'customer_name',
        'company_name',
        'address',
        'company_vat',
        'zip_code',
        'city'
    ]
    success_url = reverse_lazy('user-list')

#Allow the super user to Delete selected customer
@superuser_required()
class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete.html'
    model = User
    success_url = reverse_lazy('user-list')

@login_required()
def fortnoxauth(request):
    if request.user.is_superuser is False:
        basetemplate = 'auth1.html'
    else:
        basetemplate = 'auth.html'



    if request.method == 'GET':
        if not request.user.account_type:
            message = ""
            return render(request, 'customer/fortnoxauth.html',  {'message' : message , 'template_base' : basetemplate})
        else:
            return redirect('connect')

    elif request.method == 'POST':

        authorization = request.POST.get('auth')
        client_secret = request.POST.get('secret')

        try:
            r = requests.get(
                url="https://api.fortnox.se/3/invoices",
                headers = {
                    "Authorization-Code": authorization,
                    "Client-Secret": client_secret,
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                },
            )
            print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
            data = r.json()

            if data.get('ErrorInformation') is not None:
                message = data['ErrorInformation']['Message']
                return render(request, 'customer/fortnoxauth.html',  {'message' : message , 'template_base' : basetemplate})

            elif data.get('Authorization'):
                data = json.loads(r.content)
                access_token = data['Authorization']['AccessToken']

                results = fortnoxApiDetails.objects.create(
                    seller_id = request.user.id,
                    client_secret = client_secret,
                    access_token = access_token,
                    authorization_Code = authorization,
                )

                user1 = User.objects.get(id=request.user.id)
                user1.account_type = 'fortnox'
                user1.save()

                return redirect('connect')

        except requests.exceptions.RequestException as e:
            print('fn_authentication HTTP Request failed')
            message = "Internal Error !! try again"
            return render(request, 'customer/fortnoxauth.html',  {'message' : message , 'template_base' : basetemplate})


# class LoginView(View):
#     def get(self, request):
#         if request.method == 'POST':
#             email = request.POST.get('InputEmail1')
#             password = request.POST.get('InputPassword')
#             user = authenticate(request, username = email, password= password)
#             if user is not None:
#                 if auth.login(request, user):
#                     request.session['is_login'] = 'true'
#                     return redirect('/')
#                 else:
#                     return render(request, '401.html')
#             else:
#                 return render(request, '401.html')
#         else:
#             return render(request, '401.html')


