import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando&units=imperial&APPID=60c61be3700d4eb3171fa87fc11670c3"
request = requests.get(url)

weather_json = request.json()
print(weather_json)

main_weather = weather_json['main']

temp = main_weather['temp']

print("The Circus's current temperature is ", temp)

# must import requests module. >pip install requests

Location: c:\users\rongq\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
