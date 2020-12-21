import requests
from pprint import pprint
import settings
import csv


token = settings.GITHUB_TOKEN
headers = {'Authorization': f'token {token}'}
r = requests.get("https://api.github.com/users/aa-ag/repos")

if r.status_code == 200:
    all_repos = r.json()

    names = list()
    urls = list()

    for repo in all_repos:
        names.append(repo['name'])
        urls.append(repo['svn_url'])

    filename = "all_my_repos.csv"

    with open(filename, 'w') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(names)
        csvwriter.writerow(urls)
