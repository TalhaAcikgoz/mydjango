from rest_framework import serializers
from .models import myModel

class myModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = myModel
        fields = '__all__'

