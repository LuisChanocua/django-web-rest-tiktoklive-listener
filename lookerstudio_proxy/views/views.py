import os

from django.shortcuts import render
from django.http import JsonResponse
import requests

def daily_products_proxy(request):
    dotnet_url = os.getenv('API_INTERNAL_TOKEN', 'https://stage.promokelloggs.com/LookerStudio/DailyProducts')
    print('method:', request.method)
    print('url:', dotnet_url)
    print('headers:', request.headers)

    method = request.method
    incoming_headers = dict(request.headers)
    forced_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Content-Type': incoming_headers.get('Content-Type', 'application/json')
    }

    try:
        if method == 'GET':
            response = requests.get(dotnet_url, headers=forced_headers, params=request.GET)

        elif method == 'POST':
            body = request.body
            response = requests.post(dotnet_url, headers=forced_headers, data=body)

        else:
            return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

        print(response.json())
        return JsonResponse(response.json(), status=response.status_code, safe=False)

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)