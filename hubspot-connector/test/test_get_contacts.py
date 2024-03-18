#Importing Hubspot Class
from hubspot import HubSpot
#Import Hubspot API exceptions
from hubspot.crm.companies import ApiException
from dotenv import load_dotenv
import os

import pandas as pd

def load_access_token():
    load_dotenv()
    return os.environ['ACCESS_TOKEN']

# Create an hubspot client Instances
api_client = HubSpot(access_token=load_access_token())

try:
    #get_all() function will capture all the data from contacts object
    contact_fetched = api_client.crm.contacts.get_all()
except ApiException as e:
    print("Exception when requesting Companies by id: %s\n" % e)

print(contact_fetched)
print(contact_fetched[0])
print(contact_fetched[0].id)
print("email id is: ",contact_fetched[0].properties['email'])
print("first name is: ",contact_fetched[0].properties['firstname'])
print("last name is: ",contact_fetched[0].properties['lastname'])


print('-------------\n')
id_list = []; df =pd.DataFrame()    
for i in range(len(contact_fetched)):
    df_properties = pd.DataFrame([contact_fetched[i].properties])
    id_list.append(contact_fetched[i].id)
    df = pd.concat([df, df_properties], ignore_index=True)
df["Id"] = id_list
print(df)