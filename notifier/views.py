from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "notifier/home.html"

class AddNotes(TemplateView):
    template_name = "notifier/addnotes.html"