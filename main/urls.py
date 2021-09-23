from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.Make,name="Make new"),
    path("<str:token>/", views.Home, name="Home"),
]
