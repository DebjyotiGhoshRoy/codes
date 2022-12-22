import requests
import os
import json

token = os.environ.get("GITHUB_TOKEN")
reponame = input("repo: ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

username = input("username: ")
r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)
print(r)
