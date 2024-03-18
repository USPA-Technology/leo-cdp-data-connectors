# Data Connnector between LEO CDP and Hubspot CRM

- For HubSpot API document, please go to https://github.com/HubSpot/hubspot-api-python
- Need Hubspot Private App ACCESS_TOKEN: https://developers.hubspot.com/docs/api/private-apps

## In local Linux, follow these steps

1. Need Python 3.10, run following commands
```
sudo apt install python-is-python3
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10
sudo apt-get install python3.10-venv
pip install virtualenv
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
2. You need to refresh the session of login shell after install python-is-python3
3. Need to create a file .env to store environment variables
4. In the file .env, set value like this example
```
ACCESS_TOKEN=
