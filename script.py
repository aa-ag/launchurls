import requests
from pprint import pprint
import settings


token = settings.GITHUB_TOKEN
headers = {'Authorization': f'token {token}'}
r = requests.get("https://api.github.com/users/aa-ag")

print(r.status_code)

json = r.json()
print(json)

# for i in range(0, len(json)):
#     print("Project number: ", i+1)
#     print("Project name: ", json[i]['name'])
#     print("Project URL: ", json[i]['svn_url'], '\n')
