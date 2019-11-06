import requests
import json


# remove the minus sign
apiKey = '37134fea34fc11b5bdc5e82ad894109b3d141674'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)