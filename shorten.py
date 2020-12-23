import requests
import settings

bitly_username = settings.BITLY_USERNAME
bitly_pswd = settings.BITLY_PSWD
access_token = settings.BITLY_TOKEN


def shorten_url_with_bitly():
    # Three steps required to short urls with Bitly's API:
    # (1) generate access token,
    # (2) obtain guid,
    # (3) then shorten urls
    # ### https://dev.bitly.com/

    # (1)
    # auth_res = requests.post(
    #     'https://api-ssl.bitly.com/oauth/access_token', auth=(bitly_username, bitly_pswd))

    # if auth_res.status_code == 200:
    #     access_token = auth_res.content.decode()
    #     print(f"[!] Access token: {access_token}")
    # else:
    #     print("[!] Couldn't get access token, exiting...")
    #     exit()

    # (2)
    headers = {"Authorization": f"Bearer {access_token}"}

    group_res = requests.get(
        'https://api-ssl.bitly.com/v4/groups', headers=headers)

    if group_res.status_code == 200:
        groups_data = group_res.json()['groups'][0]
        guid = groups_data['guid']
    else:
        print("[!] Couldn't get GUID, exiting...")
        exit()

    # (3)
    url = 'https://stackoverflow.com/'
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                                json={'group_guid': guid, 'long_url': url}, headers=headers)

    if shorten_res.status_code == 200:
        shortened_url = shorten_res.json().get('link')
        print('Shortened url: ', shortened_url)


###--- driver code ---###
if __name__ == '__main__':
    shorten_url_with_bitly()
