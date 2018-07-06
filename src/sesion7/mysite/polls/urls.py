from django.conf.urls import url

from polls.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]