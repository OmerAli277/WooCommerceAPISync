from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView

from hyrportal.apps.core.models import User


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


class UserCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'user/create.html'


class UserEditView(LoginRequiredMixin, TemplateView):
    template_name = 'user/edit.html'


class UserDeleteView(LoginRequiredMixin, TemplateView):
    template_name = 'user/delete.html'
