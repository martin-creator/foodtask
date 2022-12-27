from datetime import time
import json

from django.http import JsonResponse
from coreapp.models import Order, OrderDetails, Restaurant, Meal
from coreapp.serializers import RestaurantSerializer



# =========
# CUSTOMER
# =========

def customer_get_restaurants(request):
  restaurants = RestaurantSerializer(
    Restaurant.objects.all().order_by("-id"),
    many=True,
    context={"request": request}
  ).data
  return JsonResponse({"restaurants": restaurants})