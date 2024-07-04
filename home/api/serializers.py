from rest_framework import serializers
from ..models import Blog

class BlogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    formatted_createDate=serializers.ReadOnlyField()
    formatted_updateDate=serializers.ReadOnlyField()

    class Meta:
        model=Blog
        fields=['user','user_name','title','content','img','draf','create_date','update_date','formatted_createDate','formatted_updateDate']
