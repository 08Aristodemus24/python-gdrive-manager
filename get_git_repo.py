import requests
import json
import os

from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path('./').resolve()
load_dotenv(os.path.join(BASE_DIR, '/.env'))

url = "https://api.github.com/user/repos"

accept = "application/vnd.github+json"
token = f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}"
headers = {
    "Accept": accept,
    "Authorization": token,
}
params = {
    "visibility": "all"
}

repositories = requests.get(url, headers=headers, params=params)

print("retrieved data from user" if repositories.status_code == 200 else "retrieval unsuccessful. status code {}".format(repositories.status_code))

if repositories.status_code == 200:
    for repo in repositories.json():
        print(repo.keys(), end='\n\n')
