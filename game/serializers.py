from rest_framework import serializers

from .models import *
from user.models import CustomUser
from user.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class CharacterCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = '__all__'

class RecursiveCommentSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data

class CharacterSerializer(serializers.ModelSerializer):

    skill = SkillSerializer(many=True)
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = '__all__'

    def get_total_comments(self, instance):
        return instance.character_comment.count()
