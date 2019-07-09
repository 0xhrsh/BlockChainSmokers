from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as DefaultLoginView
from codefundo.views import HomepageView


class LoginView(DefaultLoginView, HomepageView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
