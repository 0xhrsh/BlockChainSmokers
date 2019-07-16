from django.views.generic import TemplateView
from django.http import HttpResponse

class HomepageView(TemplateView):
    template_name = 'index.html'

class TestPageView(TemplateView):
    template_name = 'profile.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'

def detail(request, candidate_id):
    return HttpResponse("You're looking at candidate %s." % candidate_id)