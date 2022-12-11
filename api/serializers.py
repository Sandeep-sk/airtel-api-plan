from rest_framework import serializers
from .models import AirtelPlan


class AirtelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirtelPlan
        fields = ('__all__')

