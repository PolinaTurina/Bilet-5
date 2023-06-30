from django.urls import path
from leave_app.views import *


app_name = 'leave_app'

urlpatterns = [
    path('otpusk/', OtpuskListView.as_view()),
    path('otgul/', OtgulListView.as_view()),
    path('create/', OtpuskCreateView.as_view()),
    path('create2/', OtgulCreateView.as_view()),
    path('otkaz/<int:app_id>/', otkaz_view),
]