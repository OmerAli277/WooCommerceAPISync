from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Seller, WooProduct, WooVariant, WooOrder, WooCustomer
from woocommerce import API
import json

wcapi = API(
    url="https://sorbybacken.hyrsverige.se/",
    consumer_key="ck_eac3de02bb431d0895d1ce8bb0dc1c127adcb198",
    consumer_secret="cs_aef7c07a471db1dc10bdc11a7bd7d2e9237e6f7c",
    version="wc/v3",
    timeout=30
)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'settings.html'
    model = User
    fields = [
        'full_name',
        'company_name',
        'address',
        'company_vat',
        'city',
        'zip_code'
    ]

    success_url = reverse_lazy('settings')

    customer_page_num = 1
    """Parsing records for customers """
    while True:
        current_dict = wcapi.get("customers", params={'per_page': 1, 'page': customer_page_num}).json()
        try:
            obj = WooCustomer(customer_id=current_dict[0]['id'], first_name=current_dict[0]['first_name'],
                              last_name=current_dict[0]['last_name'], company=current_dict[0]['billing']['company'],
                              address_1=current_dict[0]['billing']['address_1'],
                              address_2=current_dict[0]['billing']['address_2'],
                              city=current_dict[0]['billing']['city'], state=current_dict[0]['billing']['state'],
                              postcode=current_dict[0]['billing']['postcode'],
                              country=current_dict[0]['billing']['country'],
                              email=current_dict[0]['billing']['email'], phone=current_dict[0]['billing']['phone'])
            obj.save()
        except:
            obj = WooCustomer(customer_id=current_dict[0]['id'], first_name=current_dict[0]['first_name'],
                              last_name=current_dict[0]['last_name'], company=current_dict[0]['billing']['company'],
                              address_1=current_dict[0]['billing']['address_1'],
                              address_2=current_dict[0]['billing']['address_2'],
                              city=current_dict[0]['billing']['city'], state=current_dict[0]['billing']['state'],
                              postcode=current_dict[0]['billing']['postcode'],
                              country=current_dict[0]['billing']['country'],
                              email=current_dict[0]['billing']['email'], phone=current_dict[0]['billing']['phone'])
        
            obj.save()
    
        if len(current_dict) > 0:
        
            customer_page_num += 1
        else:
            break

    order_page_num = 1

    """Parsing records for orders """

    while True:
        current_dict = wcapi.get("orders", params={'per_page': 1, 'page': order_page_num}).json()
        try:
            obj = WooOrder(order_id=current_dict[0]['id'], parent_id=current_dict[0]['parent_id'],
                           number=current_dict[0]['number'], order_key=current_dict[0]['order_key'],
                           created_via=current_dict[0]['created_via'],
                           version=current_dict[0]['version'],
                           status=current_dict[0]['status'], currency=current_dict[0]['currency'],
                           discount_total=current_dict[0]['discount_total'],
                           discount_tax=current_dict[0]['discount_tax'],
                           shipping_total=current_dict[0]['shipping_total'],
                           shipping_tax=current_dict[0]['shipping_tax'],
                           cart_tax=current_dict[0]['cart_tax'], total=current_dict[0]['total'],
                           total_tax=current_dict[0]['total_tax'],
                           prices_include_tax=current_dict[0]['prices_include_tax'],
                           payment_method=current_dict[0]['payment_method'],
                           payment_method_title=current_dict[0]['payment_method_title'],
                           transaction_id=current_dict[0]['transaction_id'],
                           date_created=current_dict[0]['date_created'],
                           date_modified=current_dict[0]['date_modified'],
                           date_paid=current_dict[0]['date_paid'],
                           date_completed=current_dict[0]['date_completed']
                           )
            obj.save()
        except:
            obj = WooOrder(order_id=current_dict[0]['id'], parent_id=current_dict[0]['parent_id'],
                           number=current_dict[0]['number'], order_key=current_dict[0]['order_key'],
                           created_via=current_dict[0]['created_via'],
                           version=current_dict[0]['version'],
                           status=current_dict[0]['status'], currency=current_dict[0]['currency'],
                           discount_total=current_dict[0]['discount_total'],
                           discount_tax=current_dict[0]['discount_tax'],
                           shipping_total=current_dict[0]['shipping_total'],
                           shipping_tax=current_dict[0]['shipping_tax'],
                           cart_tax=current_dict[0]['cart_tax'], total=current_dict[0]['total'],
                           total_tax=current_dict[0]['total_tax'],
                           prices_include_tax=current_dict[0]['prices_include_tax'],
                           payment_method=current_dict[0]['payment_method'],
                           payment_method_title=current_dict[0]['payment_method_title'],
                           transaction_id=current_dict[0]['transaction_id'],
                           date_created=current_dict[0]['date_created'],
                           date_modified=current_dict[0]['date_modified'],
                           date_paid=current_dict[0]['date_paid'],
                           date_completed=current_dict[0]['date_completed']
                           )
            obj.save()
    
        if len(current_dict) > 0:
        
            order_page_num += 1
        else:
            break

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        sellers = list(user.sellers.all())
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
    model = Seller
    fields = [
        'customer_no',
        'customer_name',
        'account_type',
    ]
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'user/edit.html'
    model = Seller
    fields = ['customer_no', 'customer_name', 'account_type']
    success_url = reverse_lazy('user-list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete.html'
    model = Seller
    success_url = reverse_lazy('user-list')
