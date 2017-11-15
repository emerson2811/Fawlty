# Make a get request to get the latest position of the international space station from the opennotify api.
from pip._vendor import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)

#response = requests.get("http://api.open-notify.org/iss-pass.json")
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
#parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

print(response.status_code)

# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)



# Make the same request we did earlier, but with the coordinates of San Francisco instead.
#parameters = {"lat": 37.78, "lon": -122.41}
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
#data = response.json()
#rint(type(data))
#print(data)