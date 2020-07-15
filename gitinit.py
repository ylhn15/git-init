#!/usr/bin/env python3
from github import Github
from pathlib import Path
import os
import json

def getUser(token='', user='', password=''):
    if token != '':
        github = Github(token)
    else:
        github = Github(user, password)
    return github.get_user()

def createRepo(user):
    repo_name = input("Name of the repository: ")
    repo_desc = input("Description of the repository: ")

    is_repo_private = input("Create a private repo? (y/N): ")
    is_repo_private = is_repo_private.lower() == "y"

    repository = user.create_repo(repo_name, repo_desc, private=is_repo_private)
    return { "ssh": repository.ssh_url, "html": repository.html_url }
def initializeRepo(ssh_url):
    os.system('echo "Initialize repository"')
    os.system('git init')
    os.system('echo "Remote origin"')
    os.system('git remote add origin ' + ssh_url)
    os.system('echo "Adding files"')
    os.system('git add .')
    os.system('echo "Writing initial commit"')
    os.system('git commit -m "Initial commit"')
    os.system('echo "Push Folder"')
    os.system('git push -u origin master')

def run():
    path = str(Path(__file__).parent.absolute())
    with open(path + '/config.json', 'r') as config_file:
        data = json.load(config_file)
        if 'token' not in data:
            user = data["user"]
            password = data["password"]
            user = getUser(user=user, password=password)
        else:
            auth_token = data["token"]
            user = getUser(token=auth_token)

    repo = createRepo(user)
    initializeRepo(repo["ssh"])
    print("Visit your newly create repository at: " + repo["html"])
