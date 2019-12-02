from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pulse-home'),
    path('about/', views.about, name='pulse-about'),
    path('team/', views.team, name='pulse-team'),
    path('display_results/', views.display_results, name='pulse-results'),
]
