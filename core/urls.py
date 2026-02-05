from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    path('news/', views.news, name='news'),
    
    # APIs (Data for your charts)
    path('api/market-data/', views.api_market_data, name='api_market_data'),
    path('api/stock/<str:symbol>/', views.api_stock_detail, name='api_stock_detail'),
]