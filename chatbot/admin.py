from django.contrib import admin
from .models import Chatbot
# Register your models here.


class ChatBotAdmin(admin.ModelAdmin):
    list_display = ('number', 'question', 'answer', 'options')


admin.site.register(Chatbot, ChatBotAdmin)