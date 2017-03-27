import requests
import json

result = requests.get("https://api.spotify.com/v1/artists/0OdUWJ0sBjDrqHygGUXeCF")
json_result = result.json()
pretty_result = json.loads(json_result)
print(json.dumps(pretty_result, indent=4, sort_keys=True))
