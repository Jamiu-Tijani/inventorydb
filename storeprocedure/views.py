from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *

from storeprocedure.models import stock_inventory, user

# Create your views here.


class inventory_update(generics.GenericAPIView):
    serializer_class = inventoryDataSerializer
    queryset = stock_inventory.objects.all()
    def post(self, request):
        product = request.data
        username = product["username"]
        product_title = product["product_title"]
        product_price = product["product_price"]
        product_description = product["product_description"]
        user_ =user.objects.filter(username=username)
        if user_.exists():
            userr = user.objects.get(username=username)
            stock_inventory.objects.create(user = userr,product_title = product_title,product_price=product_price,product_description=product_description)
            message = "Inventory updated sucessfully by {}".format(username)
            code = 200
            context = {
                "message": message,
                "code": code
            }
            return Response(context, status.HTTP_201_CREATED)
        else:
            message = "User Not Registered "
            code = 404
            context = {
                "message": message,
                "code": code
            }
            return Response(context, status.HTTP_401_UNAUTHORIZED)

            


class userReg(generics.GenericAPIView):
    serializer_class = userSerializer
    def post(self, request):
        user_ = request.data
        username = user_["username"]
        email = user_["email"]
        password = user_["password"]
        if user.objects.filter(username = username).exists() or user.objects.filter(email=email).exists() :
                    context = {
                    'message':'username or email already exists',
                    'code' : 300
                    }
                    return Response(context,status=status.HTTP_300_MULTIPLE_CHOICES)
        else:
                    user.objects.create_user(username, email,password)
                    user.save
                    context = {
                    'message':'user registered successfully',
                    'code' : 100

                    }
                    return Response(context,status=status.HTTP_201_CREATED)
