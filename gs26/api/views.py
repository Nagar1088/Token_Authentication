from django.shortcuts import render

# Create your views here.
from .models import student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=student.object.all()
    serializer_class=StudentSerializers
    # authentication_classes=[SessionAuthenticationAuthentication]
    # permission_classes=[IsAuthenticated]
   