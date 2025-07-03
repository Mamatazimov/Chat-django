from django.contrib import admin
from django.urls import path

from chat.views import ChatView,ChatRoomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChatView.as_view(), name='chat'),
    path('chat/<str:room_name>/', ChatRoomView.as_view(), name='room'),
]
