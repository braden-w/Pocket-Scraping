
# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "https://getpocket.com/v3/send"
  
# your source code here 
with open("4. JSON Delete Commands (Pocket Articles Tagged TIL).json", "r") as commands:
    source_code = commands.read()

# data to be sent to api 
data = {'consumer_key':"<removed for privacy>", 
        'access_token':'<removed for privacy>', 
        'actions':source_code} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text
with open("6. Post Request Output.txt", "w") as output:
    output.write(r.text )