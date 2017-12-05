import requests
from utils import formatter as f

API_URL = "https://api.github.com"
USERS = "users"
REPOS = "repos"

def list_user_repos(username):
    res = requests.get(f("{API_URL}/{USERS}/%s/{REPOS}" % username))
    json_res = res.json()
    repos_full_names = [x["full_name"] for x in json_res]
    return repos_full_names


