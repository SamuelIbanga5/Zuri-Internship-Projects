from rest_framework import serializers
from .models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('slackUsername', 'backend', 'age', 'bio')
