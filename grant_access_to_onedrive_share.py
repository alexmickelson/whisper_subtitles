import os
from pprint import pprint
import requests
import json
from dotenv import load_dotenv 
load_dotenv()


CLIENT_ID = os.environ["OFFICE_CLIENT_ID"]
CLIENT_SECRET = os.environ["OFFICE_CLIENT_SECRET"]
TENANT_ID = os.environ["OFFICE_TENNANT"]

# def get_access_token(client_id, client_secret, tenant_id):
#     url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     data = {
#         'client_id': client_id,
#         'scope': 'https://graph.microsoft.com/.default',
#         'client_secret': client_secret,
#         'grant_type': 'client_credentials'
#     }
#     response = requests.post(url, headers=headers, data=data)
#     access_token = response.json().get('access_token')
#     return access_token


# access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID)
# print(f"access token {access_token}")




# Define the API endpoint
graph_api_url = f"https://graph.microsoft.com/v1.0/users/alex.mickelson@snow.edu/drive/items/{onedrive_item_id}/invite"

# Set the sharing link and permissions
payload = {
    "recipients": [],
    "message": "",
    "requireSignIn": False,
    "sendInvitation": False,
    "roles": ["read"],  # Use ["write"] if you want edit permissions
    "link": {
        "type": "view",  # Use "edit" if you want edit permissions
        "scope": "anonymous",
        "webUrl": sharing_link
    }
}

# Set headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Send the request to grant permissions
response = requests.post(graph_api_url, json=payload, headers=headers)

if response.status_code == 200:
    print("Permissions granted successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")