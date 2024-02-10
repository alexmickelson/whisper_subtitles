import os
import requests
import json
from dotenv import load_dotenv 
load_dotenv()

# Function to get an access token
def get_access_token(client_id, client_secret, tenant_id):
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': client_id,
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    access_token = response.json().get('access_token')
    return access_token

# Function to upload a file to OneDrive
def upload_file_to_onedrive(access_token, file_path, drive_id, folder_id):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'text/plain'
    }
    file_name = file_path.split('/')[-1]
    endpoint = f'https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{folder_id}:/thename.txt:/content'
    with open(file_path, 'rb') as file_data:
        response = requests.put(endpoint, headers=headers, data="file_data as a string")

    if response.status_code == 201:
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")
        print(response.json())

# CLIENT_ID = os.environ["OFFICE_CLIENT_ID"]
# CLIENT_SECRET = os.environ["OFFICE_CLIENT_SECRET"]
# TENANT_ID = os.environ["OFFICE_TENNANT"]

# # Drive and folder details
drive_id = 'YOUR-DRIVE-ID'
folder_id = 'YOUR-FOLDER-ID'  # Folder ID or 'root' for the root folder

# # File to be uploaded
file_path = 'testfile.txt'

# Get access token

# print(f"access token: {access_token}")
upload_file_to_onedrive(access_token, file_path, drive_id, folder_id)
