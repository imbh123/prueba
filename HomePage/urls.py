from django.conf.urls import url, include
from HomePage.views import index

urlpatterns = [
    url(r'^$', index)
]