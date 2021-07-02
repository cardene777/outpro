from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from . import forms
from output.models import Output, Program


def profile(requests, username):
    outputs: list = Output.objects.filter(username=username)
    programs: list = Program.objects.filter(username=username)
    params: dict = {
        "outputs": outputs,
        "programs": programs
    }

    return render(requests, 'accounts/profile.html', params)




class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")


class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = forms.MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'


class PasswordChangeDone(generic.TemplateView):
    """パスワード変更しました"""
    template_name = 'accounts/password_change_done.html'