# Let's use python to make an API call using package called requests
# pip install requests

import requests
import json

# post_api_response = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# if post_api_response.status_code == 200:
#     print("Thanks for your request", post_api_response.status_code)
# else:
#     print("Sorry the postcode is incorrect please enter the correct postcode")


def post_code():
    user_post_code = input("Please enter your postcode")
    post_api_response = requests.get(f"https://postcodes.io/postcodes/{user_post_code}")
    if post_api_response.status_code == 200:
        print(post_api_response.content)



post_code()
















# response_bbc = requests.get("https://www.bbc.co.uk/")
# print(response_bbc)
# print(response_bbc.status_code)
# print(response_bbc.headers)

# print(type(response_bbc.content)) # bytes

# print(response_bbc.headers)
# data_headers = response_bbc.headers
#
# for data_in in data_headers:     #for data_in in data_headers.keys(): printing only keys
#     print(data_in)

# print(data_headers)
