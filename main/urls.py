from django.urls import path, include
from .views import HomepageView

app_name = 'main'

urlpatterns = [
    path('', HomepageView.as_view(template_name='main/index.html'), name='home'),
]