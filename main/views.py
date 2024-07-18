
from django.shortcuts import render
import requests
import json

def index(request):
    data = {}  # Initialize data as empty for both GET and POST requests

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            try:
                response = requests.get(
                    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e4ef7538d894b0da992fb8c53002c0a6'
                )
                response.raise_for_status()  # Raise an error for bad status codes
                list_of_data = response.json()

                data = {
                    "city": city,  # Add the city name to the data dictionary
                    "country_code": str(list_of_data['sys']['country']),
                    'coordinate': f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                    'temp': f"{list_of_data['main']['temp']} (min: {list_of_data['main']['temp_min']})",
                    'pressure': str(list_of_data['main']['pressure']),
                    'humidity': str(list_of_data['main']['humidity']),
                }
                print(data)

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"Error occurred: {req_err}")
            except json.JSONDecodeError as json_err:
                print(f"JSON decode error: {json_err}")

    return render(request, "main/index.html", {'data': data})
