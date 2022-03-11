from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def date_time_view(request):
    date = datetime.datetime.now()
    res = '<h1> The current Date and Time is at server'+str(date)+'</h1>'
    return HttpResponse(res)