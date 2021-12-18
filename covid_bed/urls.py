from django.urls import path
from . import views

app_name = "covid_bed"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('<state>/hospital_all/',views.hospital_list_view,name="hospital_list"),
    path('search/',views.searchView,name="search"),
    path("hospital/<str:id>/",views.hostpital_detail_view,name="hospital_detail"),
]
