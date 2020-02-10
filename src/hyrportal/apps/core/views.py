from django.contrib.auth import logout, hashers, login 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import WooCustomer, WooOrder, WooProduct, User
import json
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from django.contrib.auth.models import auth
# from django.contrib.auth import get_user_model
from .woo_task import woocommerce_api
# from rest_framework import generics, permissions
# from rest_framework.views import APIView
# from .serializers import UserSerialzer, CustomerSerialzer, ProductSerialzer, OrderSerialzer
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Tokens

# wcapi = API(
#     url="https://automatiseramera.se/",
#     consumer_key="ck_092c10db6a942dffe7ce610667e8c42226be7889",
#     consumer_secret="cs_0678d389f81fa5060d896e8e5fb50022626bf96b",
#     version="wc/v3",
#     timeout=30
# )
# r = wcapi.get("products")
# print(r)

# wcapi = API(
#     url="https://automatiseramera.se/",
#     consumer_key="ck_092c10db6a942dffe7ce610667e8c42226be7889",
#     consumer_secret="cs_0678d389f81fa5060d896e8e5fb50022626bf96b",
#     version="wc/v3",
#     timeout=30
# )
wp = woocommerce_api("https://automatiseramera.se/", "ck_092c10db6a942dffe7ce610667e8c42226be7889", "cs_0678d389f81fa5060d896e8e5fb50022626bf96b")
wp.sync_customers()

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
# def login(request):
#     if request.method == 'POST':
#         email = request.GET.get('InputEmail1')
#         password = request.GET.get('InputPassword')
#
#         user = auth.authenticate(username = email, password= password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'registration/login.html')
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


def signup(request):
    if request.method == 'POST':
        companyName = request.POST.get('Company_Name')
        comapanyVat = request.POST.get('Company_Vat')
        customerName = request.POST.get('Customer_Name')
        customerNum = request.POST.get('Customer_Number')
        accountType = request.POST.get('Company_Vat')
        email = request.POST.get('inputEmail')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        Address = request.POST.get('inputAddress')
        city = request.POST.get('inputCity')
        zipCode = request.POST.get('inputZip')
        BoxChecked = request.POST.get('gridCheck')

        user = User.objects.create_user(customerName, email ,password1)
        user.save()
        print('user Created')
        return render(request, 'registration/login.html')
        # if password2 == password1:
        #     return render(request, 'registration/login.html')

        # else:
        #     print ('Password not match!')
    else:
        return render(request, 'registration/signup.html')


# def get(self, request):
#     logout(request)
#     return redirect('/')

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('/')


class SettingsView(UpdateView):
    template_name = 'settings.html'
    model = User
    fields = '__all__'

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
        return self.request.user


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user/list.html'

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


class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'user/create.html'
    model = User
    fields = [
        'customer_no',
        'customer_name',
        'account_type',
    ]
    success_url = reverse_lazy('user-list')

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'user/edit.html'
    model = User
    fields = ['customer_no', 'customer_name', 'account_type']
    success_url = reverse_lazy('user-list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete.html'
    model = User
    success_url = reverse_lazy('user-list')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('user/create.html')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {form: form})
