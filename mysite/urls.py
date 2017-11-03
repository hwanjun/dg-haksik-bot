from django.conf.urls import url
from dgfoodie.views import keyboard
from dgfoodie.views import message

urlpatterns = [
    url(r'^keyboard/', keyboard),
    url(r'^message', message),
]
