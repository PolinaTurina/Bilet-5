from django.shortcuts import render
from django.views.generic import ListView
from leave_app.models import *
from leave_app.forms import *
from django.views.generic.edit import CreateView


class OtpuskListView(ListView):
    model = Otpusk
    template_name = 'leave_app/otpusk_list.html'
    context_object_name = 'otpusk_list'

    def get(self, *args, **kwargs):
        form = FilterForm(self.request.GET)
        if form.is_valid():
            filter = int(form.cleaned_data['filter'])

            if filter == 1:
                otpusk_list = self.model.objects.all()
            elif filter == 2:
                otpusk_list = self.model.objects.filter(prosmotreno=True)
            else: 
                otpusk_list = self.model.objects.filter(prosmotreno=False)

        else:
            otpusk_list = self.model.objects.all()
        return render (self.request, self.template_name, {self.context_object_name: otpusk_list, 'filter_form': form})


class OtgulListView(OtpuskListView):
    model = Otgul
    template_name = 'leave_app/otgul_list.html'
    context_object_name = 'otgul_list'


class OtpuskCreateView(CreateView):
    model = Otpusk
    fields = ['name', 'start_date', 'end_date', 'note']
    template_name = 'leave_app/form_create.html'
    success_url = '/leave-app/otpusk/'

class OtgulCreateView(CreateView):
    model = Otgul
    fields = ['name', 'date', 'note']
    template_name = 'leave_app/form_create_2.html'
    success_url = '/leave-app/otgul/'