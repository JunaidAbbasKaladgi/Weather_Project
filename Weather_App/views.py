from django.shortcuts import render
import requests


# def Home(request):
    # city = request.GET.get('city', '')
    # url = f'http://api.weatherstack.com/current?access_key=bf84622500bbca87c1efc8660a92b262&query={city}'
    # response = requests.get(url)
    # data = response.json()

    # if response.status_code == 200:
    #     payload = {
    #         'city': data['name'],
    #         'weather': data['weather'][0]['main'],
    #         'icon': data['weather'][0]['icon'],
    #         'kelvin_temperature': data['main']['temp'],
    #         'celcius_temperature': int(data['main']['temp'] - 273),
    #         'pressure': data['main']['pressure'],
    #         'humidity': data['main']['humidity'],
    #         'description': data['weather'][0]['description']
    #     }
    #     context = {'data': payload}
    # else:
    #     context = {'error_message': 'Please enter a valid city name.'}
    
    # return render(request, 'Home.html', context)
def Home(request):
    city = request.GET.get('city', '')
    
    if not city:
        return render(request, 'Home.html', {'error_message': 'Please enter a city name.'})

    API_KEY = 'bf84622500bbca87c1efc8660a92b262'  # Replace with your actual WeatherStack API key
    BASE_URL = 'http://api.weatherstack.com/current'

    url = f'{BASE_URL}?access_key={API_KEY}&query={city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if API returned valid data
        if 'current' in data and 'location' in data:
            payload = {
                'city': data['location']['name'],
                'weather': data['current']['weather_descriptions'][0],  # Weather condition
                'icon': data['current']['weather_icons'][0],  # Weather icon URL
                'celcius_temperature': data['current']['temperature'],  # Direct Celsius value
                'pressure': data['current']['pressure'],
                'humidity': data['current']['humidity'],
                'description': data['current']['weather_descriptions'][0]  # Same as 'weather'
            }
            context = {'data': payload}
        else:
            context = {'error_message': 'Invalid city name. Please try again.'}
    else:
        context = {'error_message': 'Error fetching data. Please try again later.'}
    
    return render(request, 'Home.html', context)
