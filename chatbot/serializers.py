from rest_framework import serializers
from .models import Chatbot


class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatbot
        fields = ('number', 'question', 'answer', 'options')
