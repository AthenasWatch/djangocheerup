from rest_framework import serializers
from .models import Compliment

class ComplimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliment
        fields = ('id', 'compliment', 'category')
        read_only_fields = ('id',)
        extra_kwargs = {
            'category': {'validators': []},
        }

    def validate_category(self, value):
        valid_categories = ['skills', 'trait', 'appearance']
        if value not in valid_categories:
            raise serializers.ValidationError('Invalid category')
        return value
