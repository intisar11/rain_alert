import requests
Api_keys = "a0f87bc7881e2aa18d3bd4d7bc6a465b"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=34.052235&lon=-118.243683&exclude=current,minutely,daily,alerts&appid=a0f87bc7881e2aa18d3bd4d7bc6a465b")


print(response.json()["hourly"])