"""codefundo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.TestPageView.as_view(template_name='profile.html'), name='profile'),
    path('thanks/', views.ThanksView.as_view(template_name='thanks.html'), name='thanks'),
]
