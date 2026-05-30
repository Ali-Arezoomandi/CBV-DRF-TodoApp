from rest_framework import serializers
from todo.models  import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    a serializer for Task model
    """
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'completed', 'created_date', 'absolute_url']
        read_only_fields = ['user']
        
        
    def get_absolute_url(self, obj):
        """
        put a absolute_url field for every task obj 
        """
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk) 
    
    def create(self, validated_data):
        """
        override create function to automaticlly determining user for every task obj 
        """
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)