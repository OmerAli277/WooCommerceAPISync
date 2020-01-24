from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView

from hyrportal.apps.core.models import User, Seller


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

