from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Customer, Object, Performer, Request
from .serializers import CustomerSerializer, ObjectSerializer, PerformerSerializer, RequestSerializer


# Create your views here.
class UserAPI(LoginRequiredMixin, APIView):
    def get(self, request):
        user = request.user
        userSerializer = UserSerializer(user)
        result = {
            'user': userSerializer.data,
        }
        return Response(result)


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
        return Response({'result':'ok'})

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


class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class PerformerListAPIView(generics.ListAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
