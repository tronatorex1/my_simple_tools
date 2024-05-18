# These codes show how to authenticate and pass user and password or api_key to the API in the headers variable
#   There are extra codes to show the downloaded contents or so
#   https://blog.apify.com/python-github-api/

# 1 Using the Dog API: 
import requests
api_key = 'HPTPWG9mSBOdH45WJybC9LuhnCuXCfCpNlkeB0GOcNYGXSRG5YkfHTNvYlrHNa2M'
headers = {"Content-Type": "application/json","x-api-key": api_key}
url = f"https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
response = requests.get(url=url, headers=headers).json()
pic = response[0]['url']

# Download the url's image using request and showing it with PILLOW
import urllib.request 
from PIL import Image 
urllib.request.urlretrieve(url=pic, filename="c:/tmp/x.jpg") # this allows to download a file from the url and save it locally as desired
img = Image.open("c:/tmp/x.jpg") # this uses PILLOW's resources to open in windows' Photos (the default pic browser) 
img.show()


# 2 GitHub access to my tronatorex account
import requests

base_url = "https://api.github.com/"
resource_owner = "tronatorex1"
token = "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"
access_token = "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"
header = {'Authorization': 'Bearer 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', 'X-GitHub-Api-Version': '2022-11-28'}

# 2.1 Access your user's information only
username = "tronatorex1" # github username
url = f"{base_url}users/{username}"
user_data = requests.get(url)
print(user_data.json())
print(user_data.json()['bio'])

# 2.2 Retrieve repos' names
import requests
base_url = "https://api.github.com"
username = "tronatorex1"
url = f"{base_url}/users/{username}/repos"
response = requests.get(url)
repositories_data = response.json()
print(f"Repositories of {username}:")
for repo in repositories_data:
    print(f"  - Repo: {repo['name']}")

# 2.3 Retrieve repos' names by params
import requests
base_url = "https://api.github.com"
def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
    query_params = {"sort": "updated","per_page": 5}
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        repositories_data = response.json()
        return repositories_data

username = "tronatorex1"
user_repos = get_user_repos(username)
if user_repos:
    print(f"Repositories of {username}:")
    for repo in user_repos:
        print(f"  - Repo: {repo['name']}")

# 3 Create a new repo
import requests
base_url = "https://api.github.com"
access_token = "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"
repo_name = "tronatorex3"
repo_descr = "New repo created to cluster independent tools for specific purposes. No category assigned here."
url = f"{base_url}/user/repos"
headers = {"Authorization": f"token {access_token}",}
# create json data to send using the post request
data = {"name": repo_name, "description": repo_descr,}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print(f"  + New public repo created successfully!: {new_repo}")
else:
    print(f"  X Failed to create {new_repo}")


# 4 Update a repo 
import requests
base_url = "https://api.github.com"

def update_repo_descr(access_token, username, repo_name, new_description):
    url = f"{base_url}/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {access_token}",}
    data = {"description": new_description}
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        updated_repo_data = response.json()
        return updated_repo_data

access_token = "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"
username = "tronatorex1"
repo_name = "tronatorex3"
new_description = "This is an updated description using PATCH request."
updated_repo = update_repo_descr(access_token, username, repo_name, new_description)
if updated_repo:
    print(f"Repository description has been updated.")
else:
    print("  X Failed to update the repository description.")


# 5 Delete a repo
import requests
base_url = "https://api.github.com"

def delete_repo(access_token, username, repo_name):
    url = f"{base_url}/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Repository has been deleted successfully. Status code: {response.status_code}")
    elif response.status_code == 404:
        print(f"Repository not found or already deleted. Status code: {response.status_code}")
    else:
        print(f"  X Failed to delete repository. Status code: {response.status_code}")

access_token = "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"
username = "tronatorex1"
repo_name = "tronatorex2"

delete_repo(access_token, username, repo_name)


