from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView

from .forms import FeedbackForm
from .models import Feedback
from django.views import View

# Create your views here.

# class Index(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         else:
#             form = FeedbackForm(request.POST)
#         return render(request, 'feedback/feedback.html', context={'form': form})

class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')

class ListFeedBack(TemplateView):
    template_name = 'feedback/list_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback'] = Feedback.objects.all()
        return context

class DetailFeedBack(TemplateView):
    template_name = 'feedback/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback'] = Feedback.objects.get(id=context['id_feedback'])
        return context

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
# def done(request):
#     return render(request, 'feedback/done.html')

