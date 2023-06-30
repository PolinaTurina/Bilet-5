from django.urls import path
from leave_app.views import *


app_name = 'leave_app'

urlpatterns = [
    path('otpusk/', OtpuskListView.as_view(), name='otpusk_list'),
    path('otgul/', OtgulListView.as_view(), name='otgul_list'),
    path('create/', OtpuskCreateView.as_view(), name='form_create'),
    path('create2/', OtgulCreateView.as_view(), name='form_create_2'),
    path('otkaz/<int:app_id>/', otkaz_view),
]