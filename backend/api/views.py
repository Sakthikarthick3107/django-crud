from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import ToDo
from .serializers import ToDoSerializer



class HelloWorld(APIView):
    def get(self , request):
        return Response({   
            'message' : 'Hello World',
            'info':'Hii'
        })
        
class ToDoView(APIView):
    def get(self,request , sno = None):
        if sno is not None:
            try:
                todo = ToDo.objects.get(sno = sno)
                serializer = ToDoSerializer(todo)
                return Response(serializer.data)
            except ToDo.DoesNotExist:
                return Response({'error' : 'Doesn\'t fount'} , status = status.HTTP_404_NOT_FOUND)
            
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos , many=True)
        return Response(serializer.data)
    def post(self , request):
        serializer = ToDoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    def put(self , request , sno):
        try:
            todo = ToDo.objects.get(sno = sno)
        except ToDo.DoesNotExist:
            return Response({'error' : 'Task not found'} , status = status.HTTP_404_NOT_FOUND)
        serializer = ToDoSerializer(todo , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , sno):
        try:
            todo = ToDo.objects.get(sno = sno)
        except ToDo.DoesNotExist:
            return Response({'error' : 'Task not found'} , status = status.HTTP_404_NOT_FOUND)

        todo.delete()
        return Response({ 'message' : 'Deleted successfully'},status = status.HTTP_204_NO_CONTENT)