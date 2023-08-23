from rest_framework.serializers import ModelSerializer
from .models import blog
from rest_framework import serializers

class BlogSerializer(ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model=blog
        fields=['id','name','blogtext','datetime','user']
    def create(self,validated_data):
        validated_data['user']=self.context['request'].user
        stu=blog.objects.create(**validated_data)
        return stu