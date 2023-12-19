from django.urls import path
from .views import myModelListCreateView
from .views import modelAPIListView
from .views import *
from . import views
# from .views import 

urlpatterns = [
    path("", login, name="login"),
    path('create', views.getHtmlFileToEndpoint, name='create'),
    path("user/", userpage, name='userpage'),
    path("user/api/data/", getHtmlFileToEndpoint, name='get-data')
    # path("api/", myModelListCreateView.as_view(), name="myModel"),
]