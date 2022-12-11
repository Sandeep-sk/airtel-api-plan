from django.db import models

# Create your models here.


class AirtelPlan(models.Model):
    cart_head = models.CharField(max_length=30)
    price = models.CharField(max_length=22)
    data_with_rollover = models.CharField(max_length=50)
    sms_per_day = models.CharField(max_length=22)
    local_std_and_roaming_calls = models.CharField(max_length=20)
    amazon_prime = models.CharField(max_length=20)
    
    
    def __str__(self):
        return  "plan :" + str(self.price )