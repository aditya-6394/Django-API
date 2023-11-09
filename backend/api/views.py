# from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.

def apiView(request, *args, **kwargs):
    payload = {}
    modelData  = Product.objects.all().order_by("?").first()
    if modelData:
        payload = model_to_dict(modelData, fields = ["id", "title","content","price"])
        # payload = {
        #     "title": modelData.title,
        #     "content": modelData.content,
        #     "price": modelData.price
        # }
    return JsonResponse(payload)