import requests
import os
from twilio.rest import Client

Api_keys = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get('AUTHEN_TOKEN')

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=34.052235&lon=-118.243683&exclude=current,minutely,daily,alerts&appid=a0f87bc7881e2aa18d3bd4d7bc6a465b")
response.raise_for_status()

data_2 = (response.json()['hourly'][0:11])

weather = []
for _ in data_2:
    weather_id =(_['weather'])
    for _ in weather_id:
        chances_rain = (_['id'])
        weather.append(chances_rain)

will_rain = False

for _ in weather:
    if _ > 700:
        will_rain = True


if will_rain:
    Client = Client(account_sid, auth_token)
    message = Client.messages.create(body="Bring an unbrealla",from_="+17745003472",
                                     to="+18182670211")
    print(message.sid)



