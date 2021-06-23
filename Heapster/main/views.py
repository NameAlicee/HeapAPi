from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializerList, PostSerializerDetail, AddPostSerializer


class PostsListView(APIView):
    """Ваши кучи(pepodance)"""
    permission_classes = [IsAuthenticated]
    def get(self, request):
        current_user = request.user.id
        posts = Post.objects.filter(owner=current_user)
        serializer = PostSerializerList(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        current_user = request.user
        serializer = PostSerializerList(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=current_user, status_id=1)
        return Response(serializer.data)


class PostsDetailView(APIView):
    """Ваша куча(pepodance)"""
    def get(self, request, pk):
        current_user = request.user.id
        post = Post.objects.get(id=pk, owner=current_user)
        serializer = PostSerializerDetail(post)
        return Response(serializer.data)




