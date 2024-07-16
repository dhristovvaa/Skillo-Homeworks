import requests
import json


url = "https://jsonplaceholder.typicode.com/todos/1"


response = requests.get(url)


if response.status_code == 200:
    # Parse the JSON response
    data = response.json()


    with open('response.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print(f"Request failed with status code: {response.status_code}")

#response.json
