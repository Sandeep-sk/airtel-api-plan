from django.contrib import admin
from django.urls import path,include
from .views import get_latest_plans,AirtelPlanApi
from rest_framework import routers


router = routers.DefaultRouter()
router.register("plans",AirtelPlanApi)

urlpatterns = [
path('',get_latest_plans),
path('', include(router.urls)),
]
