# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response
from user.models import CustomUser
from .permissions import *
from .serializers import *

class GameList(generics.ListCreateAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CharacterList(generics.ListCreateAPIView):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CharacterCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def update(self, request, *args, **kwargs):
        serializer = CharacterCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillList(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CommentList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        user = CustomUser.objects.get(username=request.user)
        comment_count = Comment.objects.filter(character=self).exclude(deleted=True).count()
        character = Character.objects.get(username=request.user)
        character.count_comment = comment_count
        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrReadOnly]