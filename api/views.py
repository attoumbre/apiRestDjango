# from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView,Response

class DumpItAPI(APIView):
    
    def get(self,request):
        items = [
            "apple",
            "mango",
            "grapes"
        ]
        response_data = {"datas":items}
        return Response(response_data,status=status.HTTP_200_OK)