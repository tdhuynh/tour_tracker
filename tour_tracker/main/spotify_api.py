import requests

name = input('band name: ').lower()
result = requests.get("https://api.spotify.com/v1/artists/0OdUWJ0sBjDrqHygGUXeCF")
json_result = result.json()

if name == json_result['name'].lower():
    print(json_result['name'])
else:
    print('artist does not exist')
