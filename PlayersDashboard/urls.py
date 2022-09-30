from django.urls import path
from . import views


urlpatterns = [
   path('', views.homepage),
   path('stats-table', views.search_player),
   path('players/', views.get_positions_info), 
   path('regression/', views.get_regression),
]
