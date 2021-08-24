
from django.http import response
from django.urls import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response 

class Loginview(APIView):

    def post(self, request):
        response ={}
        response['status']= 500
        response['message']='something went wrong try again'

        try:
            data = request.data
            
            if data.get('username') is None:
                response['message']='something went wrong try again'
                
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message']='something went wrong try again'
                
                raise Exception('key password not found')
        
        except Exception as e :
            print (e)
        
        return response(response)