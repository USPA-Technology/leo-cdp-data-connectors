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
    
def build_bizfly_payload(emails:str, name:str, address:str):
    # config = BizflyConfig(source='redis', redis_port=6480)
    config = BizflyConfig()
    bizfly_app_key = config.bizfly_app_key
    bizfly_token = config.bizfly_token
    bizfly_project_token = config.bizfly_project_token
    
    print(bizfly_app_key)
    print(bizfly_token)
    print(bizfly_project_token)
    
    # Prepare the payload as a dictionary
    payload = {
        'app_key': bizfly_app_key,
        'token': bizfly_token,
        'project_token': bizfly_project_token,
        'list': 'b2b4f225-970f-41ea-bb46-6c5c3371ba60',
        'emails': emails,
        'phones':'0903122290',
        'name': name,
        'gender': 'male',
        "address": address,
        "birthday":"16/08/1986",
        "tongMuaHang":3000.11,
        "cdp_dataLabels":"test, demo",
        "dataLabels": ["demo","test"],
        "segments": ["male","customer"],
        "lastest_purchased_date":None,
    }
    return payload
    
def send_contact_to_bizfly(payload):
    if payload is None:
        print("Error: payload is None. Please call build_bizfly_payload to build valid payload")
        return
    
    # Set headers (optional, add if needed)
    headers = {'Content-Type': 'application/json'}  

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

payload = build_bizfly_payload('trieu@leocdp.com',"Trieu","Ho Chi Minh City")
send_contact_to_bizfly(payload)