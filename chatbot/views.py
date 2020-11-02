from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ChatBotSerializer
from .models import Chatbot


class Chatbot(viewsets.ModelViewSet):
    serializer_class = ChatBotSerializer
    queryset = Chatbot.objects.all()
