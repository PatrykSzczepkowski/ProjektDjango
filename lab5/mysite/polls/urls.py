from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/', views.osoba_list),
    path('osoba/<int:pk>/', views.osoba_detail),
    path('osobazn/<str:znaki>',views.osoba_list_str),
    path('stanowisko/<int:pk>/', views.stanowisko_detail),
    path('stanowisko/', views.stanowisko_list),
]