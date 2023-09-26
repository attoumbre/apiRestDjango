# from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Item
from .serializers import ItemSerializer


class DumpItAPI(APIView):
    
    def get(self,request):
        items = Item.objects.all()
        items_data = ItemSerializer(items,many=True).data
        response_data = {"datas":items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        name = request.data.get('name')
        Item.objects.create(name=name)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)