import requests
import datetime
API_KEY = "92dfffc0f7df4fdfd3aa43171e3e3b8e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
city = input("Which city do you want to check? ").capitalize()
request_url = f'{BASE_URL}appid={API_KEY}&q={city}'
#Below code checks to see if the there are any errors in the request URL
check_error = requests.get(request_url)
#Error code 200 means that the URL is OK. Anything else means an HTTP error.

if check_error.status_code == 200:
    results = check_error.json()
    weather = results['weather'][0]['description']
    temperature = round(results["main"]["temp"] - 273.15, 0)
    country = results['sys']['country']
    print(f' It is currently {temperature} degrees Celcius in {city},{country} and the conditions are {weather}')
else:
    print(f'Ooops! Something went wrong with the request')
    print(f'Error code:{check_error}')
    #If there is an error, you can check what the error code means on https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
