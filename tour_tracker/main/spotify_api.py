import requests

result = requests.get("https://api.spotify.com/v1/artists/{id}")
print(result)
json_result = result.json()
print(json_result)
