from django.shortcuts import render
from django.views.generic import *

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        return context

#class DatosVisitaView(TemplateView):
    