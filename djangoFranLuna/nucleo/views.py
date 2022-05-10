from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def fecha_actual(request):
    hoy=datetime.datetime.now()
    html="<html><body>Hoy es %s</body></html>" % hoy
    return HttpResponse(html)
