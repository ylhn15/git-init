#!/usr/bin/env python3
import os
import json
from pathlib import Path
from getpass import getpass
from github import Github


def create_config():
    credentials = {}
    path = str(Path(__file__).parent.absolute()) + '/config.json'
    config_file = Path(path)
    if config_file.is_file() is not True:
        print("Do you want to use credentials or a token for authorization? ")
        auth_type = input("(c)redentials/(t)oken: ")
        if auth_type.lower() == 'c' or auth_type.lower() == 'credentials':
            credentials['user'] = input("username: ")
            credentials['password'] = getpass()
        else:
            credentials['token'] = input("token: ")

        f = open(path, 'w')
        f.write(json.dumps(credentials))


def getUser(token='', user='', password=''):
    if token != '':
        github = Github(token)
    else:
        github = Github(user, password)
    return github.get_user()


def create_repo(user):
    repo_name = input("Name of the repository: ")
    repo_desc = input("Description of the repository: ")

    is_repo_private = input("Create a private repo? (y/N): ")
    is_repo_private = is_repo_private.lower() == "y"

    repository = user.create_repo(repo_name, repo_desc,
            private=is_repo_private)
    return {
            "ssh": repository.ssh_url,
            "html": repository.html_url,
            "repo_name": repo_name
           }


def initialize_repo(ssh_url, repo_name):
    os.system('echo "# "' + repo_name + ' >> README.md')
    os.system('echo "Initialize repository"')
    os.system('git init')
    os.system('echo "Remote origin"')
    os.system('git remote add origin ' + ssh_url)
    os.system('echo "Adding files"')
    os.system('git add .')
    os.system('echo "Writing initial commit"')
    os.system('git commit -m "Initial commit"')
    os.system('echo "Push Folder"')
    os.system('git push --set-upstream origin main')


def get_authorization():
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
        return user


def run():
    create_config()
    user = get_authorization()
    repo = create_repo(user)
    initialize_repo(repo["ssh"])
    print("Visit your newly create repository at: " + repo["html"])
