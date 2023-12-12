from django.contrib.auth.models import User
from .serialaizers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserAPI(LoginRequiredMixin, APIView):
    def get(self, request):
        user = request.user
        userSerializer = UserSerializer(user)
        result = {
            'user': userSerializer.data,
        }
        return Response(result)
