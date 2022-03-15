from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
# Create your views here.

class PostViews(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViews(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


