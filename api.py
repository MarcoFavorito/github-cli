import requests
import json
from utils import formatter as f
import getpass

API_URL = "https://api.github.com"
USERS   = "users"
USER    = "user"
REPOS   = "repos"
REPO    = "repo"


def get_users_repos(username):
    res = requests.get(f("{API_URL}/{USERS}/%s/{REPOS}" % username))
    json_res = res.json()
    return json_res

def post_user_repos(username, data):
    password = getpass.getpass()
    res = requests.post(f("{API_URL}/{USER}/{REPOS}"), data=json.dumps(data), auth=(username, password))
    json_res = res.json()
    return json_res

def delete_user_repo(username, name):
    password = getpass.getpass()
    res = requests.delete(f("{API_URL}/{REPOS}/%s/%s" % (username, name)), auth=(username, password))
    print(res)
    print(res.text)
    return True




