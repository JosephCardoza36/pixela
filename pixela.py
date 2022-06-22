import requests
from datetime import datetime

# https://pixe.la/v1/users/josephc/graphs/graph1.html

USERNAME = 'josephc'
TOKEN = 'a76ujytf49ijty6uk'
pixela_url = 'https://pixe.la/v1/users'
headers = {
    'X-USER-TOKEN': TOKEN  #use password
}

#pip install requests

#---------------------------CREATE USER--------------------------#

# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
#
# # response = requests.post(url=pixela_url, json=user_params)
# # print(response.text)

#---------------------------------CREATE GRAPH-----------------------------#

# graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"
#
# # graph_config = {
# #     'id': 'graph1',
# #     'name': 'Coding Daily',
# #     'unit': 'hour',
# #     'type': 'int',
# #     'color': 'sora'
# # }
# #
# # # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # #
# # # print(response.text)

#-----------------------------POST DATA----------------------------#

# today = datetime(year=2022, month=6, day=14) #previous day(s)!
today = datetime.now()

pixel_create = f"{pixela_url}/{USERNAME}/graphs/graph1"
pixel_params = {
    'date': today.strftime('%Y%m%d'),  #organize time to be YEAR|MONTH|DAY
    'quantity': input("How many hours did you code?: ")
}

response = requests.post(url=pixel_create, json=pixel_params, headers=headers)

print(response.text)   #prints if successful