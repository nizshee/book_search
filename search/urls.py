from django.conf.urls import url

from . import views


urlpatterns = [
    # <city_name> - how it works?
    url(r'^city/(?P<city_name>\w*)$', views.find_city, name='city_search'), 
    url(r'^book/(?P<city_name>\w*)$', views.find_book, name='book_search'), 
]