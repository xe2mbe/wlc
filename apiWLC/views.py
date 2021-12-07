from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apiWLC.serializers import GuestUserSerializer, APSerializer
from apiWLC.models import guestuser, ap


class GuestUserViewSet(viewsets.ModelViewSet):
   queryset = guestuser.objects.all()
   serializer_class = GuestUserSerializer


class APViewSet(viewsets.ModelViewSet):
   queryset = ap.objects.all()
   serializer_class = APSerializer