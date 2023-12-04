from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/', views.osoba_list),
    path('osoba/<int:pk>/', views.osoba_detail),
    path('osoba/update/<int:pk>/', views.osoba_update),
    path('osoba/delete/<int:pk>/', views.osoba_delete),
    path('osobazn/<str:znaki>',views.osoba_list_str),
    path('stanowisko/<int:pk>/', views.stanowisko_detail),
    path('stanowisko/', views.stanowisko_list),
    path('stanowisko/<int:pk>/members/', views.stanowisko_members),
]