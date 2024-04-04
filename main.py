import requests
import json


# Define a function for running on AWS Lambda
def lambda_handler(event, context): 
    # Request authentication token for calling LibCal api
    
    ## Set up parameter for the request
    auth_url = "https://cuhk.libcal.com/1.1/oauth/token"
    data = {
        "grant_type": "grant_type", # Please change "grant_type" to your own
        "client_id": "your_client_id", # Please change "your_client_id" to your own
        "client_secret": "your_client_secret", # Please change "your_client_secret" to your own
    }
    
    ## Request & read token from the response
    auth_response = requests.post(auth_url, data=data).json()
    auth_token = auth_response["access_token"]
    
    # Use auth_token to make API calls
    
    ## Define header for making API calls that will hold authentication data
    
    api_url = "your_libcal_calendar_api_url" # Please change "your_libcal_calendar_api_url" to your own
    headersAPI = {
        'accept': 'application/json',
        'Authorization': "Bearer %s" % auth_token,
    }
    
    api_response = requests.get(api_url, headers=headersAPI, verify=True).json()
    
    # Extra data from the response
    dataList = api_response["events"]
    eventList = []
    
    # Print and massage the data
    i = 0
    for data in dataList:
        date = data["start"].replace("T", " ").replace(":00+08:00", "").split(" ")[0]
        startTime = data["start"].replace("T", " ").replace(":00+08:00", "").split(" ")[1]
        endTime = data["end"].replace("T", " ").replace(":00+08:00", "").split(" ")[1]
        
        event = {
            "id": str(data["id"]),
            "title": data["title"],
            "date": date,
            "startTime": startTime,
            "endTime": endTime,
            "url": data["url"]["public"],
        }
        
        eventList.append(event)
    
    return eventList