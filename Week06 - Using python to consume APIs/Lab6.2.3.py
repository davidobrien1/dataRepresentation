

import requests
import json



apiKey = '99d587abba8e104052bb27e54aa8a57012a3ec41'
url = 'https://api.github.com/davidobrien1/PrivateRepository'
filename ="hello.py"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)