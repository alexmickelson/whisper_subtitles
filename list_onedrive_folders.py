

import json
from pprint import pprint
import requests




# Query the Microsoft Graph API for the drives
# url = 'https://graph.microsoft.com/v1.0/me/drives'
# headers = {'Authorization': 'Bearer ' + access_token}
# response = requests.get(url, headers=headers)
# pprint(response.json())
# # Print the drives
# drives = response.json()['value']
# for drive in drives:
#     print(drive['id'], drive['name'])

endpoint = ''

# Define the headers for the API request
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Make the API request to retrieve the list of files
response = requests.get(endpoint, headers=headers)
print(json.dumps(response.json(), indent=4))
# Parse the response JSON to extract the file names
files = response.json()['value']
for file in files:
    if file['name'] == '1810-spring-2024':
        pprint(file)