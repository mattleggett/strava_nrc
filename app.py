from pprint import pprint as pp
import json
import requests

# all of your activity since the the start of the time epochs
url = 'https://api.nike.com/sport/v3/me/activities/after_time/0'

# input b64 bearer token found using the readme steps
token = ''

auth = {
    'Authorization': f'Bearer {token}'
}

results = requests.get(url, headers=auth)  # currently not working

# res.json file generated using curl currently
# curl -v -H "Authorization: Bearer ${BearerToken}" 'https://api.nike.com/sport/v3/me/activities/after_time/0' > res.json

with open('res.json', 'r') as f:
    results = json.load(f)

activities = results['activities']
