 
from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate_name(self, value):
        if value['name'] == value['description']:
            raise serializers.ValidationError("Title and description should not be the same")
        return value
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name should be greater than 2 characters")
        return value
