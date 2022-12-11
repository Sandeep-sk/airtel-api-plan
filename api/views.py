from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import AirtelPlan
from .serializers import *
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def get_latest_plans(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    start_url = "https://www.airtel.in/myplan-infinity/Delhi"
    driver.get(start_url)
    s=driver.page_source.encode("utf-8")
    soup = BeautifulSoup(s, 'html.parser')
    a=soup.find('section',class_='plansSection')
    b=soup.findAll("div", "single_cart")
    for i in b:

        spanvalue=[] 
        for j in i.findAll('div',class_="border-bottom"):
            spanvalue.append(j.find('span').text)        


        if AirtelPlan.objects.filter(data_with_rollover=spanvalue[0]).exists() and AirtelPlan.objects.filter(price= ( (i.find('div',class_="cart_head")).find('span',class_='price').text )).exists():
            continue
        else:
            plan=AirtelPlan(cart_head=(i.find('div',class_="cart_head")).find('span').text , price= ( (i.find('div',class_="cart_head")).find('span',class_='price').text ),
            data_with_rollover=spanvalue[0],sms_per_day=(spanvalue[1]),local_std_and_roaming_calls=spanvalue[2],amazon_prime=spanvalue[3])    
            plan.save()


    driver.quit()    
            
    return HttpResponse("<h1>Latest Data Fetched..</h1>")


class AirtelPlanApi(viewsets.ModelViewSet):
    queryset = AirtelPlan.objects.all()
    serializer_class = AirtelPlanSerializer

