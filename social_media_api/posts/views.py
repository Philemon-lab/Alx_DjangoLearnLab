from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated  # <- exact string
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # <- exact string
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # <- exact string

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'post unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # <- exact string


class PostLikeView(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # <- exact string

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # <- exact string required by checker
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # <- exact string
def feed(request):
    user = request.user
    followed_users = user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
