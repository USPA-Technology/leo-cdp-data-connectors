import requests, os, redis
from dotenv import load_dotenv
load_dotenv(override=True)


# Define the URL
CLIENT_CODE = 'dgv'
BIZFLY_BASE_URL_CONTACT = "https://apicampaign.bizfly.vn/api/customer/contact/import"

class BizflyConfig:
    def __init__(self, source='env', redis_host='localhost', redis_port=6379, redis_db=0):
        if source == 'env':
            self.bizfly_app_key = os.environ['bizfly_app_key']
            self.bizfly_token = os.environ['bizfly_token']
            self.bizfly_project_token = os.environ['bizfly_project_token']
        elif source == 'redis':
            r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
            self.bizfly_app_key = r.get(CLIENT_CODE + '_bizfly_app_key').decode('utf-8')
            self.bizfly_token = r.get(CLIENT_CODE +'_bizfly_token').decode('utf-8')
            self.bizfly_project_token = r.get(CLIENT_CODE +'_bizfly_project_token').decode('utf-8')
        else:
            raise ValueError("Source must be 'env' or 'redis'")

    def __repr__(self):
        return (f"BizflyConfig(bizfly_app_key={self.bizfly_app_key}, "
                f"bizfly_token={self.bizfly_token}, "
                f"bizfly_project_token={self.bizfly_project_token})")
    
def send_contact_to_bizfly():
    
    config = BizflyConfig(source='redis', redis_port=6480)
    bizfly_app_key = config.bizfly_app_key
    bizfly_token = config.bizfly_token
    bizfly_project_token = config.bizfly_project_token
    
    print(bizfly_app_key)
    print(bizfly_token)
    print(bizfly_project_token)
    
     # Set headers (optional, add if needed)
    headers = {'Content-Type': 'application/json'}  
    
    # Prepare the payload as a dictionary
    payload = {
        'app_key': bizfly_app_key,
        'token': bizfly_token,
        'project_token': bizfly_project_token,
        'list': '',
        'emails': 'thomas1@example.com',
        'name': 'Thomas Moore 1',
        "address": "Vietnam"
    }

    # Send the POST request with JSON payload
    response = requests.post(BIZFLY_BASE_URL_CONTACT, json=payload, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        # Get the response data
        data = response.json()
        print(data)
    else:
        # Handle error
        print(f"Error: {response.status_code}")
        print(response.text)


send_contact_to_bizfly()