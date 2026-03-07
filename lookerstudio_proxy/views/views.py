import os

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
import requests

def daily_products_proxy(request):
    endpoint_suffix = 'LookerStudio/DailyProducts'  # Cambia esto según el endpoint que quieras usar
    apiUrl = os.getenv(f'API_BASE_URL_KELLANOVA', f'https://stage.promokelloggs.com/')
       
    apiCallUrl = f'{apiUrl}{endpoint_suffix}'
    print('method:', request.method)
    print('url:', apiCallUrl)
    print('headers:', request.headers)

    method = request.method
    incoming_headers = dict(request.headers)
    forced_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Content-Type': incoming_headers.get('Content-Type', 'application/json')
    }

    try:
        if method == 'GET':
            response = requests.get(apiCallUrl, headers=forced_headers, params=request.GET)

        elif method == 'POST':
            body = request.body
            response = requests.post(apiCallUrl, headers=forced_headers, data=body)

        else:
            return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        print(response.json())
        return JsonResponse(response.json(), status=response.status_code, safe=False)

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def daily_users_proxy(request):
    
    endpoint_suffix = 'LookerStudio/DailyUsers'  # Cambia esto según el endpoint que quieras usar
    apiUrl = os.getenv(f'API_BASE_URL_KELLANOVA', f'https://stage.promokelloggs.com/')
    
    apiCallUrl = f'{apiUrl}{endpoint_suffix}'
    print('method:', request.method)
    print('url:', apiCallUrl)
    print('headers:', request.headers)

    method = request.method
    incoming_headers = dict(request.headers)
    forced_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Content-Type': incoming_headers.get('Content-Type', 'application/json')
    }

    try:
        if method == 'GET':
            response = requests.get(apiCallUrl, headers=forced_headers, params=request.GET)

        elif method == 'POST':
            body = request.body
            response = requests.post(apiCallUrl, headers=forced_headers, data=body)

        else:
            return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        print(response.json())
        return JsonResponse(response.json(), status=response.status_code, safe=False)

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)