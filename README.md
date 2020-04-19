
# Pocket-Scraping
Using Python, JSON, and HTTP GET/POST requests to interface with the Pocket API and retrieve/delete tagged entries.
This specific project deletes all Pocket entries with the tag "TIL."

# To Use

 1. Modify "[0. Pocket Web TIL Scraper.json](https://github.com/bmw02002turbo/Pocket-Scraping/blob/master/0.%20Pocket%20Web%20TIL%20Scraper.json)" to match the properties of Pocket entries that you want to delete.
 2. Run "[1. Post Request to Retrieve Pocket.py](https://github.com/bmw02002turbo/Pocket-Scraping/blob/master/1.%20Post%20Request%20to%20Retrieve%20Pocket.py)" to generate JSON Data of matching Pocket entries as "2. JSON Data (Pocket Articles Tagged TIL).json".
 3. Run "[3. Generate Deletion Commands.py](https://github.com/bmw02002turbo/Pocket-Scraping/blob/master/3.%20Generate%20Deletion%20Commands.py)" to generate delete commands for  Pocket entries as "4. JSON Delete Commands (Pocket Articles Tagged TIL).json".
 4. Run "[5. Post Request to Delete Pocket.py](https://github.com/bmw02002turbo/Pocket-Scraping/blob/master/5.%20Post%20Request%20to%20Delete%20Pocket.py)" to delete and generate server output as "6. Post Request Output.txt".
 5. Hopefully your output file should generate “action_results”:[true,true,…]∎! Enjoy!
