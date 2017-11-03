from django.conf.urls import url
from dgfoodie.views import keyboard

urlpatterns = [
    url(r'^keyboard/', keyboard),
]
