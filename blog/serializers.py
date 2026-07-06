
from rest_framework import serializers
from .models import Post,Comment, Category
from django.contrib.auth.models import User


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name','description','slug']

class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name']

class PostSerializer(serializers.ModelSerializer):
    category =SimpleCategorySerializer(read_only=True)
    author =SimpleUserSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
    queryset=Category.objects.all(),
    source="category",
    write_only=True
)
    class Meta:
        model = Post 
        fields = ['id','category','category_id','title','content','slug','author','featured_image','is_published','created_at','updated_at']

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['id','title','slug']
          
          
class CommentSerializer(serializers.ModelSerializer):
    author =SimpleUserSerializer(read_only=True)
    post =SimplePostSerializer(read_only=True)

    post_id = serializers.PrimaryKeyRelatedField(
    queryset=Post.objects.all(),
    source="post",
    write_only=True
)
    class Meta:
        model = Comment
        fields =['id','post','post_id','author','content','created_at']
       
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
