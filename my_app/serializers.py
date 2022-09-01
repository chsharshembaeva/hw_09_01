from rest_framework import serializers
from .models import Employee, Position


class PositionSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position = validated_data.get('position')
        instance.department = validated_data.get('department')
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    date_birth = serializers.DateTimeField()
    position = serializers.CharField(source='position.position', max_length=100)
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.date_birth = validated_data.get('date_birth')
        instance.position = validated_data.get('position')
        instance.salary = validated_data.get('salary')
        instance.save()
        return instance



