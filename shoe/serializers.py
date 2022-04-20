from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shoe.models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        price = attrs.get('price')
        
        if price <= 0:
            raise ValidationError("Price must be greater than 0")
        
        return attrs
    
    class Meta:
        model = Shoe
        fields = ('id', 'name', 'price', 'description')