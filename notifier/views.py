from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from .forms import AppointmentForm
from .models import Appointment
# Create your views here.
class HomeView(TemplateView):
    template_name = "notifier/home.html"

    def get(self, request, *args, **kwargs):
        data = Appointment.objects.all()
        return render(request,self.template_name,{"data": data})

class AppointmentFormView(View):
    form_class = AppointmentForm
    initial = {'key': 'value'}
    template_name = 'notifier/appointmentForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            # return HttpResponseRedirect("Done")

        return render(request, self.template_name, {'form': form})