import requests
from pprint import pprint
import settings


token = settings.GITHUB_TOKEN
owner = 'aa-ag'
repo = 'gitignore'
query_url = f"https://api.github.com/repos/{owner}/{repo}"

params = {
    'state': 'open'
}

headers = {'Authorization': f'token {token}'}

r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())
