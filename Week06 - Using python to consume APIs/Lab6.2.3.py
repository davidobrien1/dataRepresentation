

import requests
import json



apiKey = '905e55f8abc9af793d3032b1485bc97382f086dd'
url = 'https://api.github.com/davidobrien1/PrivateRepository'
filename ="davidprivaterepo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)