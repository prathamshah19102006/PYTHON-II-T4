from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models  import Student,Book
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers import StudentSerializer,BookSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    if request.method=='GET':
        Books=Book.objects.all()
        serializer=BookSerializer(Books,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        # student=Student.objects.all()
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # saves to DB
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # if request.method=='GET':
    #     student=Student.objects.all()
    #     serializer=StudentSerializer(student,many=True)
    #     return Response(serializer.data)
    # elif request.method=='POST':
    #     # student=Student.objects.all()
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()  # saves to DB
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


