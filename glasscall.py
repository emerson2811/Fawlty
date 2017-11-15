from pip._vendor import requests

response = requests.get(
    "http://api.glassdoor.com/api/api.htm?v=1.1&t.p=227327&t.k=dTQp1xB5saU&userip=206.208.217.6&useragent=Mozilla/%2F4.0&format=json&v=1&action=jobs-stats&returnStates=true&admLevelRequested=1")
print(response.status_code)
print(response.content)