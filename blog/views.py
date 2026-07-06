
from .models import Post,Category,Comment
from .serializers import PostSerializer, CommentSerializer,CategorySerializer,RegisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.db.models import Q

from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PostPagination,CommentPagination
from .permissions import IsAuthorOrReadOnly

class CategoryViewSet(ModelViewSet):
    serializer_class= CategorySerializer
    queryset =Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title','content']
    ordering_fields = ['created_at','title']
    ordering = ['-created_at']
    pagination_class = PostPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(
            Q(is_published=True) |
            Q(author=self.request.user)
        ).select_related("author", "category")

        return Post.objects.filter(is_published=True).select_related("author", "category")
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['post', 'author']
    search_fields = ['content']
    ordering_fields =['created_at']
    ordering= ['-created_at']
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.filter(post__is_published=True).select_related("author","post")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

