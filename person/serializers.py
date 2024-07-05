from rest_framework import serializers
from .models import Department, Person


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ("id",)

    # Know the count of people in each department
    person_count = serializers.SerializerMethodField()
    def get_person_count(self, obj):
            return obj.person_set.count()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ("id","start_date", "updated_date",)



    # show department name in Person 
    department_name = serializers.SerializerMethodField()
    def get_department_name(self, obj):
            return obj.department.name