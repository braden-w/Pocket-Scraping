# importing the requests library 
import requests
import json 
  
# defining the api-endpoint  
API_ENDPOINT = "https://getpocket.com/v3/get"
  
# data to be sent to api  (from source code)
with open("0. Pocket Web TIL Scraper.json", "r") as commands:
    params = json.loads(commands.read())

headers = {"Host":"getpocket.com", "Content-Type":"application/json"}

# sending post request and saving response as response object 
r = requests.get(API_ENDPOINT, params = params) 

# extracting response text
with open("2. JSON Data (Pocket Articles Tagged TIL).json", "w") as output:
    output.write(json.dumps(json.loads(r.text), indent=4))