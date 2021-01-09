# Import a library that allows to make HTTP request

import requests


# Set the API endpoint
#Include http(s) in the URL
url = input("Input URL: ")


# Use the library to perform an HTTP GET request to the URL

response = requests.get(url)


# Print out the data

print(response.text)