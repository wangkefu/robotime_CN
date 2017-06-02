from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from robotime_cn_website.models import RtProduct


def index(request):
    return render(request, 'index.html')

def ImageSupport(request):

    return render(request, 'ImageSupport.html')

def DesignTeam(request):
    products= RtProduct.objects.all()

    return render(request, 'DesignTeam.html',{'products':products})

def CompanyHistory(request):
    print RtProduct.objects.all()

    return render(request, 'CompanyHistory.html')



