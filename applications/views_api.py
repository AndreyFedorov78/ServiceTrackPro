import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Object, Request, Region
from .serializers import CustomerSerializer, ObjectSerializer, ObjectSerializer2, RequestSerializer
from .serializers import UserSerializer, UserListSerializer, RegionSerializer


def get_related_models(model):
    related_fields = {}
    for field in model._meta.fields:
        if isinstance(field, models.ForeignKey):
            related_fields[field.name] = field.related_model
    return related_fields


class RegionAPIView(LoginRequiredMixin, APIView):
    @staticmethod
    def post(request):
        region = Region.objects.all()
        regionSerializer = RegionSerializer(region, many=True)
        result = regionSerializer.data
        return Response(result)

    @staticmethod
    def put(request):
        id = request.data.get('id')
        if id is None:
            Response({}, status=status.HTTP_400_BAD_REQUEST)
        if id:
            region = Region.objects.get(pk=id)
        else:
            region = Region()
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(LoginRequiredMixin, APIView):
    def get(self, request):
        user = request.user
        userSerializer = UserSerializer(user)
        result = {
            'user': userSerializer.data,
        }
        return Response(result)


class UserListAPI(APIView):
    def get(self, request):
        users = User.objects.filter(is_active=True).order_by("last_name", "first_name")

        # Создаем объект "не выбран" и добавляем его в начало списка
        not_selected = User(id=None, last_name="не", first_name="выбран")
        users = [not_selected] + list(users)

        user_serializer = UserListSerializer(users, many=True)
        return Response(user_serializer.data)


class CustomerListAPIView_____(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListAPIView(LoginRequiredMixin, APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    @staticmethod
    def post(request):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer(queryset, many=True)
        result = serializer_class.data
        return Response(result)

    @staticmethod
    def put(request):
        id = request.data.get('id')
        if id is None:
            Response({}, status=status.HTTP_400_BAD_REQUEST)
        if id:
            customer = Customer.objects.get(pk=id)
        else:
            customer = Customer()
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class CustomerAPIView(APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, id):
        if id == 0:
            return Response(CustomerSerializer(Customer()).data)

        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def delete(self, request, id):
        try:
            Customer.objects.get(id=id).delete()
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': 'ok'})

    def put(self, request, id):

        if id == 0:
            customer = Customer()
        else:
            customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestAPIView(APIView):
    @staticmethod
    def get(request, id):
        if id == 0:
            request_ = Request()
            request_.request_date = datetime.date.today()
            if request.user.is_authenticated:
                request_.created_by = request.user
            else:
                # костыль для отладки без авторизации
                request_.created_by = User.objects.all()[0]
            return Response(RequestSerializer(request_).data)
        request_ = get_object_or_404(Request, id=id)
        serializer = RequestSerializer(request_)
        return Response(serializer.data)

    @staticmethod
    def delete(request, id):
        try:
            Request.objects.get(id=id).delete()
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': 'ok'})

    @staticmethod
    def put(request, id):
        # получаем поля модели
        fields = Request._meta.fields
        field_names = [field.name for field in fields]

        #  поля с дадами
        dates = [
            field.name for field in fields
            if isinstance(field, models.DateField)
        ]
        # поля ссылки
        relatedList = get_related_models(Request)
        # print(relatedList.keys())

        if id == 0:
            request_ = Request()
        else:
            request_ = get_object_or_404(Request, id=id)
        for attr, value in request.data.items():
            if attr not in field_names or attr == 'id':
                continue
            # переформатируем даты
            if attr in dates:
                value = value[0:10] if value is not None else value
            # переформатируем объекты
            if attr in relatedList and value is not None:
                id = value if isinstance(value, int) else value['id']
                try:
                    value = relatedList[attr].objects.get(id=id)
                except:
                    return Response({}, status=status.HTTP_400_BAD_REQUEST)

            try:
                setattr(request_, attr, value)
            except:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        request_.save()
        # except:
        #    Response({}, status=status.HTTP_400_BAD_REQUEST)

        return Response({})


class ObjectAPIView(APIView):
    @staticmethod
    def get(request, id):
        if id == 0:
            object_ = Object()
            if request.user.is_authenticated:
                object_.responsible = request.user
            return Response(ObjectSerializer(object_).data)
        object = get_object_or_404(Object, id=id)
        serializer = ObjectSerializer(object)

        return Response(serializer.data)

    @staticmethod
    def delete(request, id):
        try:
            Object.objects.get(id=id).delete()
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': 'ok'})

    @staticmethod
    def put(request, id):
        if id == 0:
            object_ = Object()
        else:
            object_ = get_object_or_404(Object, id=id)
        for attr, value in request.data.items():
            if attr == 'customer':
                try:
                    value = Customer.objects.get(id=value['id'])
                except:
                    value = None
            if attr == 'responsible':
                try:
                    value = User.objects.get(pk=value['id'])
                except:
                    value = None
            try:
                setattr(object_, attr, value)
            except:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        try:
            object_.save()
        except:
            Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ObjectSerializer(object_)
        return Response(serializer.data)


class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer2


class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
