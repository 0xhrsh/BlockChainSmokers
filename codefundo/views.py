from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import Candidate, Constituency
from django.views import generic


class ProfilePageView(TemplateView):
    template_name = 'codefundo/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class VoteHelperPageView(TemplateView):
    template_name = 'codefundo/helper.html'

    def get_context_data(self, **kwargs):
        context = super(VoteHelperPageView, self).get_context_data()
        context['candidates'] = Candidate.objects.all()
        return context


class ThanksView(TemplateView):
    template_name = 'codefundo/thanks.html'


class DetailView(generic.DetailView):
    model = Candidate
    template_name = 'codefundo/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data()
        context['candidates'] = Candidate.objects.all()
        return context

# def vote(request, constituency_id):
#     constituency = get_object_or_404(Constituency, pk=constituency_id)
#     try:
#         selected_choice = constituency.candidate_set.get(pk=request.POST['candidate'])
#     except (KeyError, Candidate.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'codefundo/helper.html', {
#             'constituency': constituency,
#             'error_message': "You didn't select a candidate.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('helper', args=(constituency.id,)))


