from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
