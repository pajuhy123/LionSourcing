from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_sourcing),
    url(r'^practice$', views.practice_sourcing, name ='practice'),
    url(r'^send$', views.send_fb, name='send_fb'),
    url(r'^next$', views.next_sentence, name='next'),
    url(r'^save$', views.index_save, name='index_save'),
    url(r'^readme$', views.readme, name='readme'),
]