

from django.urls import path
from . import views
from .views import HomeView, CollectdbView, CollectdbView002

urlpatterns = [
    path('', HomeView.as_view(), name="home"),


    path('collectingdb', CollectdbView.as_view(), name="collectingdb"),
    path('collectingdb002', CollectdbView002.as_view(), name="collectingdb002"),
    path('successori2',views.successori2 , name="successori2"),
    path('successree2',views.successree2 , name="successree2"),    

]
