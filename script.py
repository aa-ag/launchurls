import requests
from pprint import pprint
import settings


token = settings.GITHUB_TOKEN
headers = {'Authorization': f'token {token}'}
r = requests.get("https://api.github.com/users/aa-ag/repos")

if r.status_code == 200:
    all_repos = r.json()

    for repo in all_repos:
        print(repo['name'] + ' | ' + repo['svn_url'])
