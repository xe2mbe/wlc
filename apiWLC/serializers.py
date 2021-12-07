from django.db import models
from rest_framework import serializers

from apiWLC.models import guestuser, ap

class GuestUserSerializer(serializers.ModelSerializer):
   class Meta:
       model = guestuser
       fields = '__all__'


class APSerializer(serializers.ModelSerializer):
   class Meta:
       model = ap
       fields = '__all__'