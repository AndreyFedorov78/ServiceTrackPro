from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer, Object,  Request, Region, Facility


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "name"]

    def get_name(self, obj):
        return f"{obj.last_name} {obj.first_name} {'(' + obj.username + ')' if obj.id is not None else ''}"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ObjectSerializer(serializers.ModelSerializer):
    responsible = UserListSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Object
        fields = '__all__'

class ObjectSerializer2(serializers.ModelSerializer):
    sub_name = serializers.SerializerMethodField()
    responsible = UserListSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Object
        fields = '__all__'

    def get_sub_name(self, obj):
        return f'{obj.customer.name} : "{obj.name}"'



class RequestSerializer(serializers.ModelSerializer):
    created_by=UserListSerializer()
    object = ObjectSerializer2()
    class Meta:
        model = Request
        fields = '__all__'
