

import requests
import json

url = "https://reqbin.com/echo/get/json"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the response content as JSON in a file
    with open("response.json", "w") as json_file:
        json.dump(response.json(), json_file, indent=2)
    print("Response saved as 'response.json'.")
else:
    print(f"Error: Failed to make the request. Status code: {response.status_code}")
