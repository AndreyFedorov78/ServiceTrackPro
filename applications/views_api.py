from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Object,  Request
from .serializers import CustomerSerializer, ObjectSerializer,  RequestSerializer
from .serializers import UserSerializer, UserListSerializer


# Create your views here.
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


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


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
        print("STARTING")
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
                Response({}, status=status.HTTP_400_BAD_REQUEST)
            try:
                object_.save()
            except:
                Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ObjectSerializer(object_)
        return Response(serializer.data)


class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer



class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
