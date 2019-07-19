from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as DefaultLoginView
from codefundo.views import HomepageView
from .models import Profile, User


class LoginView(DefaultLoginView, HomepageView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()
