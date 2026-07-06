from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PostViewSet, CommentViewSet,RegisterView

urlpatterns = [

path("register/", RegisterView.as_view()),

]

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns += router.urls

