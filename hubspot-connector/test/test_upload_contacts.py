# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:46:23 2022
@author: user
"""

from hubspot import HubSpot
from hubspot.crm.companies import SimplePublicObjectInput
from hubspot.crm.companies import ApiException
import pandas as pd

from dotenv import load_dotenv
import os

def load_access_token():
    load_dotenv()
    return os.environ['ACCESS_TOKEN']

# initialize list of lists
data = [['7', 'Ronaldo', 'Cristiano', 'Ronaldo dos Santos Aveiro', "cr7@manchesterunited.com"], 
        ["8", "Mata", "Juan", "Manuel Mata García", "juanmata@manchesterunited.com"], 
        ['18', "Fernandes", "Bruno", 'Miguel Borges Fernandes', "br18@manchesterunited.com"]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['jersey_number', 'player_name', 'firstname', 'lastname',
                                 'email'])

#or you can load the data using
#df = pd.read_csv("your_filename.csv")  # reading csv file
# df = pd.read_excel("yourfilename.xlxs", sheet_name = "your_sheet_name")

#####here we are going to upload or create a new data 

#we will create an Dictionary
insert_record_dict = [ {k:v for k,v in m.items() if pd.notnull(v)} for m in df.to_dict(orient='records')]

#Initializing the API Client
api_client = HubSpot(access_token=load_access_token())

try:
    #Create a list that will store the contact id generated while creation of the list
    list_id = []
    for idx in range(len(insert_record_dict)):
        simple_public_object_input = SimplePublicObjectInput(
            properties=insert_record_dict[idx]
        )
        
        
        api_response = api_client.crm.contacts.basic_api.create(
             simple_public_object_input_for_create=simple_public_object_input
         )
        print(api_response)
        store_api_response_companies = api_response
        list_id.append(api_response.id)
except ApiException as e:
    print("Exception when creating contact: %s\n" % e)
print(list_id)