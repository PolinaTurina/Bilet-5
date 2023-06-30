from django.shortcuts import render
from django.views.generic import ListView
from leave_app.models import *


class OtpuskListView(ListView):
    model = Otpusk
    template_name = 'leave_app/otpusk_list.html'
    context_object_name = 'otpusk_list'
