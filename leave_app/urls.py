from django.urls import path
from leave_app.views import *


app_name = 'leave_app'

urlpatterns = [
    path('otpusk/', OtpuskListView.as_view()),
    path('otgul/', OtgulListView.as_view()),
]