# Generates deletion 

import json
with open('2. JSON Data (Pocket Articles Tagged TIL).json', 'r',encoding="cp866") as f:
    id_dict = json.load(f)

output = ""

for entry_id in id_dict["list"]:
    output+= f"""
    {{
        "action" : "delete",
        "item_id" : "{entry_id}"
    }},"""

output = f"[{output[:-1]}]"

with open('4. JSON Delete Commands (Pocket Articles Tagged TIL).json', "w") as output_file:
    output_file.write(output)