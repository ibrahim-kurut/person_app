from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from .models import Department, Person
from .serializers import DepartmentSerializer, PersonSerializer


from .permissions import IsAdminOrReadOnly

# Create your views here.

#? _____________ Create New Department _____________
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    '''
        Adding permissions to Department so that only the admin can deal with them
        Only other users can see the Department
    '''
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]






#? _____________ Create New Person _____________
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    '''
        Adding permissions to Department so that only the admin can deal with them
        Only other users can see the Department
    '''
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Add user ID who created the user
        serializer.save(user=request.user)
        print("user--------------> " , request.user)
  
        return Response({
            'message': 'Person created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


