import requests, os
from dotenv import load_dotenv
load_dotenv(override=True)

bizfly_app_key = os.environ['bizfly_app_key']
bizfly_token = os.environ['bizfly_token']
bizfly_project_token = os.environ['bizfly_project_token']

print(bizfly_app_key)
print(bizfly_token)
print(bizfly_project_token)

# Define the URL
url = "https://apicampaign.bizfly.vn/api/customer/contact/import"

# Prepare the payload as a dictionary
payload = {
    'app_key': bizfly_app_key,
    'token': bizfly_token,
    'project_token': bizfly_project_token,
    'list': '',
    'emails': 'thomas@example.com',
    'name': 'Thomas Moore',
    "address": "Vietnam"
}

# Set headers (optional, add if needed)
headers = {'Content-Type': 'application/json'}  # Example header

# Send the POST request with JSON payload
response = requests.post(url, json=payload, headers=headers)


# Check for successful response
if response.status_code == 200:
    # Get the response data
    data = response.json()
    print(data)
else:
    # Handle error
    print(f"Error: {response.status_code}")
    print(response.text)
