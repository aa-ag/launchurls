##--- IMPORTS ---##
import requests
from pprint import pprint
import settings
import csv
import webbrowser
import pprint
import requests
import settings


##--- GLOBAL VARIABLES ---##
github_token = settings.GITHUB_TOKEN
github_username = settings.GITHUB_USER
# https://docs.github.com/en/free-pro-team@latest/rest/reference/users
github_headers = {'Authorization': f'token {github_token}'}
# r = requests.get(f"https://api.github.com/users/{user}/repos")
# "A call to List public repositories provides paginated items in sets of 30,
# whereas a call to the GitHub Search API provides items in sets of 100
# You can specify how many items to receive (up to a maximum of 100)"
r = requests.get(
    f"https://api.github.com/users/{github_username}/repos?per_page=3")

github_user = requests.get(f'https://api.github.com/users/{github_username}')
public_repos_count = github_user.json()['public_repos']
print(public_repos_count)  # if < 100, script needs to consider pagination

bitly_username = settings.BITLY_USERNAME
bitly_pswd = settings.BITLY_PSWD
bitly_access_token = settings.BITLY_TOKEN
bitly_guid = settings.BITLY_GUID


##--- FUNCTIONS ---##


def get_links_from_github(req):
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
        # [!] optional
        short_urls = [shorten_urls_with_bitly(link) for link in urls]

        # create a file where data will be saved to
    filename = "all_repos.csv"

    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["#", "Repo Name", "URL"])
        csv_writer.writerows(
            zip([i + 1 for i in range(len(names))], names, short_urls))


def shorten_urls_with_bitly(link):
    url = f'{link}'
    # Three steps required to short urls with Bitly's API:
    # (1) generate access token,
    # (2) obtain guid,
    # (3) then shorten urls
    # ### https://dev.bitly.com/

    # (1)
    # auth_res = requests.post(
    #     'https://api-ssl.bitly.com/oauth/access_token', auth=(bitly_username, bitly_pswd))

    # if auth_res.status_code == 200:
    #     bitly_access_token = auth_res.content.decode()
    #     print(f"[!] Access token: {bitly_access_token}")
    # else:
    #     print("[!] Couldn't get access token, exiting...")
    #     exit()

    # (2)
    bitly_headers = {"Authorization": f"Bearer {bitly_access_token}"}

    # group_res = requests.get(
    #     'https://api-ssl.bitly.com/v4/groups', headers=bitly_headers)

    # if group_res.status_code == 200:
    #     groups_data = group_res.json()['groups'][0]
    #     guid = groups_data['guid']
    #     print(guid)
    # else:
    #     print("[!] Couldn't get GUID, exiting...")
    #     exit()

    # (3)
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                                json={'group_guid': bitly_guid, 'long_url': url}, headers=bitly_headers)

    if shorten_res.status_code == 200:
        shortened_url = shorten_res.json().get('link')
        return shortened_url


def open_links(all_repos):
    # Once 'all_repos' has been created by get_links(),
    # read the csv file and open all url's using webbrowser.
    # Iterating thru each row as they're each a list
    with open(all_repos) as all_repos_csv:
        csv_reader = csv.reader(all_repos_csv)
        for row in csv_reader:
            webbrowser.open_new_tab(row[2])


##--- DRIVER CODE ---##
# if __name__ == '__main__':
#     get_links_from_github(r)
#     open_links('all_repos.csv')
