##--- IMPORTS ---##
import requests
from pprint import pprint
import settings
import csv
import webbrowser
import pprint


##--- GLOBAL VARIABLES ---##
github_token = settings.GITHUB_TOKEN
github_username = settings.GITHUB_USER
# https://docs.github.com/en/free-pro-team@latest/rest/reference/users
headers = {'Authorization': f'token {github_token}'}
# r = requests.get(f"https://api.github.com/users/{user}/repos")
# "A call to List public repositories provides paginated items in sets of 30,
# whereas a call to the GitHub Search API provides items in sets of 100
# You can specify how many items to receive (up to a maximum of 100)"
r = requests.get(
    f"https://api.github.com/users/{github_username}/repos?per_page=100")


##--- FUNCTIONS ---##


def get_links(req):
    # Checks if request gets successful response
    # if so, iterates over the all repos as a json object
    # and makes two lists: one with names, another with urls.
    # Finally, creates CSV file with resulting data
    if req.status_code == 200:
        all_repos = req.json()

        # TEST: seeing data structure
        # for i in all_repos:
        #     pprint.pprint(i)

        names = list()
        urls = list()

        for repo in all_repos:
            names.append(repo['name'])
            urls.append(repo['svn_url'])

        # shorten URL's
        # INSERT HERE

    # create a file where data will be saved to
    filename = "all_repos.csv"

    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["#", "Repo Name", "URL"])
        csv_writer.writerows(
            zip([i + 1 for i in range(len(names))], names, urls))


def open_links(all_repos):
    # Once 'all_repos' has been created by get_links(),
    # read the csv file and open all url's using webbrowser.
    # Iterating thru each row as they're each a list
    with open(all_repos) as all_repos_csv:
        csv_reader = csv.reader(all_repos_csv)
        for row in csv_reader:
            webbrowser.open_new_tab(row[2])


##--- DRIVER CODE ---##
if __name__ == '__main__':
    get_links(r)
    # open_links('all_repos.csv')
