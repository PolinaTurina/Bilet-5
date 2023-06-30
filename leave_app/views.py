from django.shortcuts import render, redirect
from django.views.generic import ListView
from leave_app.models import *
from leave_app.forms import *
from django.views.generic.edit import CreateView
# from django.shortcuts import redirect


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



def otkaz_view(request, app_id):
    if request.method == "POST":
        if 'is_otpusk' in request.POST and request.POST.get('is_otpusk') == True:
            application = Otpusk.objects.get(id=app_id)
            object_type = 'otpusk'
        else:
            application = Otgul.objects.get(id=app_id)
            object_type = 'otgul'

        form = OtkazForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            application.prosmotreno = True

            if cd['odobreno']:
                application.save()
            else:
                otkaz = Otkaz(note=cd['note'], name=cd['name'])
                otkaz.save()

                application.otkaz = otkaz
                application.save()
            return redirect(f'/leave-app/{object_type}/')
    else:
        form = OtkazForm()

    return render(request, 'leave_app/otkaz.html', {'form': form})