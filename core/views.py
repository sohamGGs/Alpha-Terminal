from django.shortcuts import render
from django.http import JsonResponse
from .models import Stock
import random

# --- Views (Pages) ---
def dashboard(request):
    return render(request, 'dashboard.html', {'active_tab': 'dashboard'})

def analytics(request):
    stocks = Stock.objects.all()
    return render(request, 'analytics.html', {'active_tab': 'analytics', 'stocks': stocks})

def news(request):
    return render(request, 'news.html', {'active_tab': 'news'})

# --- APIs (Data) ---
def api_market_data(request):
    """Sends fake live data to the frontend"""
    data = {
        'indices': [
            {'name': 'NIFTY 50', 'price': 22430.00, 'change': 0.45},
            {'name': 'BANKNIFTY', 'price': 47800.50, 'change': -0.12},
        ],
        'gainers': [
            {'symbol': 'TATASTEEL', 'ltp': 156.40, 'change': 2.4, 'volume': '12M'},
            {'symbol': 'RELIANCE', 'ltp': 2980.00, 'change': 1.8, 'volume': '5M'},
        ],
        'losers': [
            {'symbol': 'HDFCBANK', 'ltp': 1420.00, 'change': -1.5, 'volume': '8M'},
        ]
    }
    return JsonResponse(data)

def api_stock_detail(request, symbol):
    """Sends fake analysis data for a specific stock"""
    return JsonResponse({
        'symbol': symbol,
        'z_score': round(random.uniform(1.5, 4.5), 2),
        'debt_equity': round(random.uniform(0.1, 2.0), 2),
        'volatility': round(random.uniform(10, 30), 1),
        'price': round(random.uniform(100, 3000), 2),
    })