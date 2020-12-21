##--- IMPORTS ---##
import requests
from pprint import pprint
import settings
import csv


##--- GLOBAL VARIABLES ---##
token = settings.GITHUB_TOKEN
headers = {'Authorization': f'token {token}'}
r = requests.get("https://api.github.com/users/aa-ag/repos")


##--- FUNCTIONS ---##
def get_links():
    global r
    # Checks if request gets successful response
    # if so, iterates over the all repos as a json object
    # and makes two lists: one with names, another with urls.
    # Finally, creates CSV file with resulting data
    if r.status_code == 200:
        all_repos = r.json()

        names = list()
        urls = list()

        for repo in all_repos:
            names.append(repo['name'])
            urls.append(repo['svn_url'])

        filename = "all_repos.csv"

    with open(filename, 'w') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerows(zip(names, urls))


##--- DRIVER CODE ---##
if __name__ == '__main__':
    get_links()
