from django.shortcuts import render
import requests


def Home(request):
    city = request.GET.get('city', '')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a6fc42c07d9ec25392435d30cb600119'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        payload = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'kelvin_temperature': data['main']['temp'],
            'celcius_temperature': int(data['main']['temp'] - 273),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        context = {'data': payload}
    else:
        context = {'error_message': 'Please enter a valid city name.'}
    
    return render(request, 'Home.html', context)
