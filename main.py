import requests

x = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username=soft.hubtr',headers={'x-ig-app-id': "936619743392459"})
response = x.json()
print(response["data"]["user"]["biography"])