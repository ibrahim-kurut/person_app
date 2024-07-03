from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


from .models import Department, Person
from .serializers import DepartmentSerializer, PersonSerializer

# Create your views here.

#? _____________ Create New Department _____________
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer






#? _____________ Create New Person _____________
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

