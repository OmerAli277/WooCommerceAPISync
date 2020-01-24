from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, FormView


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SettingsForm(ModelForm):
    class Meta:
        model = User


class SettingsView(LoginRequiredMixin, FormView):
    template_name = 'settings.html'
    form_class = SettingsForm


class UserCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'user/create.html'


class UserEditView(LoginRequiredMixin, TemplateView):
    template_name = 'user/edit.html'


class UserDeleteView(LoginRequiredMixin, TemplateView):
    template_name = 'user/delete.html'
