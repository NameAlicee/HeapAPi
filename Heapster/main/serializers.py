from rest_framework import serializers

from .models import Post


class PostSerializerList(serializers.ModelSerializer):

    status = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Post
        fields = ("title", "status", "date_posted", "result")


class PostSerializerDetail(serializers.ModelSerializer):

    status = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Post
        exclude = ()


class AddPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


