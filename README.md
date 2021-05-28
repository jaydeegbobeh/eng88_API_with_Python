# What is an API
## API with python

### Application programming Interface
**An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices. To simplify, an API delivers a user response to a system and sends the system's response back to a user.**

api.postcodes.io/postcodes/
A directory for all UK postcodes


```
import requests
import json

post_api_response = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
if post_api_response.status_code == 200:
    print("Thanks for your request", post_api_response.status_code)
else:
    print("Sorry the postcode is incorrect please enter the correct postcode")
```
This code checks if a postcode is a valid UK postcode, if it is it returns the code 200 and gives information such as latitude.
```
import requests
import json
def post_code():
    user_post_code = input("Please enter your postcode\n")
    post_api_response = requests.get(f"https://postcodes.io/postcodes/{user_post_code.lower()}")
    if post_api_response.status_code == 200:
        print(json.dumps(post_api_response.json(), indent=1))


post_code()
```
