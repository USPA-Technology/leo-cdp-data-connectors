import requests

app_id = ""
client_secret = ""
redirect_uri = "https://zalo-apps.bigdatavietnam.org/callback"

# Step 2: Construct authorization URL (Refer to Zalo docs for exact format)
auth_url = "https://openapi.zalo.me/v2.0/oa/authorize?"

# Step 4: Suppose you receive the auth code 'xyz123' in the redirect  
code = ""

# Step 5: Token Request 
token_endpoint = "https://oauth.zaloapp.com/v4/oa/access_token"  
data = {
    "app_id": app_id,
    "grant_type": 'authorization_code',
    "code": code
}

response = requests.post(token_endpoint, data=data)

print(response.content)
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"] 
    print(f"Access Token: {access_token}")
else:
    print("Failed to get access token")
