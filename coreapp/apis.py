from datetime import time
import json

from django.http import JsonResponse
from coreapp.models import Order, OrderDetails, Restaurant, Meal
from coreapp.serializers import RestaurantSerializer, MealSerializer



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

def customer_get_meals(request, restaurant_id):
  meals = MealSerializer(
    Meal.objects.filter(restaurant_id=restaurant_id).order_by("-id"),
    many=True,
    context={"request": request}
  ).data
  return JsonResponse({"meals": meals})

def customer_add_order(request, restaurant_id):
  return JsonResponse({})

def customer_get_latest_order(request, restaurant_id):
  return JsonResponse({})
