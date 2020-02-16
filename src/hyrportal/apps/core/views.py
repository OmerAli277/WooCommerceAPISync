from django.contrib.auth import logout, hashers, login 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

from hyrportal import settings
from .models import WooCustomer, WooOrder, WooProduct, User
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

# class UsersViewSet(generics.ListCreateAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerialzer


# class GetUserView(generics.RetrieveUpdateAPIView):

#     serializer_class = UserSerialzer

#     def get_queryset(self):
#         print(self.kwargs.get('pk'))
#         return User.objects.filter(id=self.kwargs.get('pk'))

# class GetToken(APIView):
#     """
#     GetToken
#     """
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, _format=None):
#         """
#         {
#         "password":"asdf1234",
#         "username":"hanif"
#         }
#         """
#         user = User.objects.get(username=request.data.get("username"))
#         if not user:
#             return Response({"success": False, "Message": "user does not exist"})
        
#         token = None
#         if hashers.check_password(request.data.get("password"), user.password):
#             token, _ = Token.objects.get_or_create(user=user)
#             login(request, user)
#         return Response({"success": True, "Message": "successful", "token": token.key if token else None})


#

def connect(request):
    return render(request, 'customer/connect.html')


class LoginView(View):
    def get(self, request):
        print('I am in LoginView')
        if request.method == 'POST':
            email = request.POST.get('InputEmail1')
            print(email)
            password = request.POST.get('InputPassword')
            print(password)
            user = authenticate(request, username = email, password= password)
            if user is not None:
                auth.login(request, user)
                print('User logged In')
                request.session['is_login'] = 'true'
                return redirect('/')
            else:
                return render(request, 'registration/signup.html')
        else:
            return render(request, 'registration/login.html')

def request(request):
    print('I am in Login')
    if request.method == 'POST':
        email = request.POST.get('InputEmail1')
        print(email)
        password = request.POST.get('InputPassword')
        print(password)
        user = authenticate(request, username = email, password= password)
        if user is not None:
            auth.login(request, user)
            print('User logged In')
            request.session['is_login'] = 'true'
            return redirect('/')
        else:
            return render(request, 'registration/signup.html')
    else:
        return render(request, 'registration/login.html')



# def login_view(request):
#     print('I am in Login')
#     if request.method == 'POST':
#         email = request.POST.get('InputEmail1')
#         print(email)
#         password = request.POST.get('InputPassword')
#         print(password)
#         user = authenticate(request, username = email, password= password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'registration/signup.html')
#     else:
#         return render(request, 'registration/login.html')


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('user/create.html')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {form: form})

@user_passes_test(lambda u: u.is_superuser)
def signup(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            companyName = request.POST.get('Company_Name')
            print(companyName )
            comapanyVat = request.POST.get('Company_Vat')
            print(comapanyVat)
            user_name = request.POST.get('User_Name')
            print(user_name)
            customerNum = request.POST.get('Customer_Number')
            print(customerNum)
            accountType = request.POST.get('Company_Vat')
            print(accountType)
            email = request.POST.get('inputEmail')
            print(email)
            password1 = request.POST.get('password1')
            print(password1)
            password2 = request.POST.get('password2')
            print(password2)
            Address = request.POST.get('inputAddress')
            print(Address)
            city = request.POST.get('inputCity')
            print(city)
            zipCode = request.POST.get('inputZip')
            print(zipCode)
            BoxChecked = request.POST.get('gridCheck')
            print(BoxChecked)
            CustomerName = request.POST.get('CustomerName')
            print(CustomerName)

            if password2 == password1:
                user = User.objects.create_user(username=user_name, email=email ,password=password1 , company_name=companyName,
                                                address=Address, city=city, zip_code=zipCode, customer_name = CustomerName,
                                                customer_no=customerNum )

                user.save()
                print('user Created')
                return redirect('/')
            else:
                print('Password not matched.')
                message = 'Password not matched!'
                return render(request, 'registration/signup.html', {'message' : message})
        else:
            return render(request, 'registration/signup.html')

    else:
        html = "<html><body>Access Denied.%s.</body></html>"
        return HttpResponse(html)


# def get(self, request):
#     logout(request)
#     return redirect('/')

class LogoutView(View):

    def get(self, request,  *args, **kwargs):
        print('In LogOut')
        del request.session['is_login']
        logout(request)
        return redirect('/')


def home_page(request):
    print("home_page")
    is_login = request.session.get('is_login' , 'false')
    print('session value ' + request.session.get('is_login' , 'false'))
    if is_login == 'false':
        print('not_login')
        # return render(request, 'registration/login.html')
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.user.is_superuser:
            print('superuser_login')
            return redirect('settings')
            # return render(request, 'settings.html')
        else:
            print('customer_login')
            return redirect('customer-settings')
            # return render(request, 'customer/settings.html')



def cus(request):
    print('In Cus')
    return render(request, 'customer/settings.html')

class CustomerSettingsView(UpdateView):
    template_name = 'customer/settings.html'
    model = User
    fields = [
        'customer_name',
        'company_name',
        'address',
        'company_vat',
        'zip_code',
        'city'
    ]

    success_url = reverse_lazy('customer-settings')

    def get_object(self, *args, **kwargs):
        print("Customer Settings View")
        return self.request.user


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper



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
        'city'
    ]

    success_url = reverse_lazy('settings')

    # success_url = reverse_lazy('settings')

    # customer_page_num = 1
    # """Parsing records for customers """
    # while True:
    #     current_dict = wcapi.get("customers", params={'per_page': 1, 'page': customer_page_num}).json()
    #     for i in current_dict:
    #             # print(i)
    #             # obj = WooCustomer(customer_id=i['id'], first_name=i[0]['first_name'])
    #             # obj.save()
    #         try:
    #             obj, created  = WooCustomer.objects.update_or_create(customer_id=i['id'], first_name=i['first_name'],
    #                               last_name=i['last_name'], company=i['billing']['company'],
    #                               address_1=i['billing']['address_1'],
    #                               address_2=i['billing']['address_2'],
    #                               city=i['billing']['city'], state=i['billing']['state'],
    #                               postcode=i['billing']['postcode'],
    #                               country=i['billing']['country'],
    #                               email=i['email'], phone=i['billing']['phone'], date_created=i['date_created'],
    #                               date_modified=i['date_modified'], is_paying_customer=i['is_paying_customer'])
    #         except:
    #             pass
    #     if len(current_dict) > 0:
    #         customer_page_num += 1
    #     else:
    #         break
    #
    # order_page_num = 1
    #
    # """Parsing records for orders """
    #
    # while True:
    #     current_dict = wcapi.get("orders", params={'per_page': 1, 'page': order_page_num}).json()
    #     try:
    #         obj = WooOrder(order_id=current_dict[0]['id'], parent_id=current_dict[0]['parent_id'],
    #                        number=current_dict[0]['number'], order_key=current_dict[0]['order_key'],
    #                        created_via=current_dict[0]['created_via'],
    #                        version=current_dict[0]['version'],
    #                        status=current_dict[0]['status'], currency=current_dict[0]['currency'],
    #                        discount_total=current_dict[0]['discount_total'],
    #                        discount_tax=current_dict[0]['discount_tax'],
    #                        shipping_total=current_dict[0]['shipping_total'],
    #                        shipping_tax=current_dict[0]['shipping_tax'],
    #                        cart_tax=current_dict[0]['cart_tax'], total=current_dict[0]['total'],
    #                        total_tax=current_dict[0]['total_tax'],
    #                        prices_include_tax=current_dict[0]['prices_include_tax'],
    #                        payment_method=current_dict[0]['payment_method'],
    #                        payment_method_title=current_dict[0]['payment_method_title'],
    #                        transaction_id=current_dict[0]['transaction_id'],
    #                        date_created=current_dict[0]['date_created'],
    #                        date_modified=current_dict[0]['date_modified'],
    #                        date_paid=current_dict[0]['date_paid'],
    #                        date_completed=current_dict[0]['date_completed']
    #                        )
    #         obj.save()
    #     except:
    #         obj = WooOrder(order_id=current_dict[0]['id'], parent_id=current_dict[0]['parent_id'],
    #                        number=current_dict[0]['number'], order_key=current_dict[0]['order_key'],
    #                        created_via=current_dict[0]['created_via'],
    #                        version=current_dict[0]['version'],
    #                        status=current_dict[0]['status'], currency=current_dict[0]['currency'],
    #                        discount_total=current_dict[0]['discount_total'],
    #                        discount_tax=current_dict[0]['discount_tax'],
    #                        shipping_total=current_dict[0]['shipping_total'],
    #                        shipping_tax=current_dict[0]['shipping_tax'],
    #                        cart_tax=current_dict[0]['cart_tax'], total=current_dict[0]['total'],
    #                        total_tax=current_dict[0]['total_tax'],
    #                        prices_include_tax=current_dict[0]['prices_include_tax'],
    #                        payment_method=current_dict[0]['payment_method'],
    #                        payment_method_title=current_dict[0]['payment_method_title'],
    #                        transaction_id=current_dict[0]['transaction_id'],
    #                        date_created=current_dict[0]['date_created'],
    #                        date_modified=current_dict[0]['date_modified'],
    #                        date_paid=current_dict[0]['date_paid'],
    #                        date_completed=current_dict[0]['date_completed']
    #                        )
    #         obj.save()
    #
    #     if len(current_dict) > 0:
    #
    #         order_page_num += 1
    #     else:
    #         break
    def get_object(self, *args, **kwargs):
        print("Settings View")
        return self.request.user

@superuser_required()
class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user/list.html'
    model = User

    # def head(self):
    #     customer = User.first_name + ' ' + User.last_name
    #     print(customer)

    def get_context_data(self, **kwargs):
        print ('get_context_data ')
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

@superuser_required()
class UserCreateView(LoginRequiredMixin, CreateView):
    # template_name = 'user/create.html'
    template_name = 'registration/signup.html'

    fields = [
        'customer_no',
        'customer_name',
        'account_type',
    ]
    success_url = reverse_lazy('user-list')

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)

@superuser_required()
class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'user/edit.html'
    model = User
    fields = [
        'customer_no',
        'customer_name',
        'account_type'
    ]
    success_url = reverse_lazy('user-list')

@superuser_required()
class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete.html'
    model = User
    success_url = reverse_lazy('user-list')

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return redirect('user/create.html')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {form: form})
