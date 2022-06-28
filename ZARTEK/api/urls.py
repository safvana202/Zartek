from django.urls import path
from . import views


urlpatterns = [
    path('images',views.getPosts),
    path('addlikes',views.addlikes),
    
]