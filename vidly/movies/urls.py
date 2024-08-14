from django.urls import path
from . import views

# movies/  this is the root of this app
# movies/1/details
urlpatterns = [
    path('', views.index, name='index')
]
