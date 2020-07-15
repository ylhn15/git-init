#### Description
Create and initialize a GitHub Repo in the current folder.

#### Authorization
Create a config.json file.

##### Github Token
To use a private GitHub Token, add the following to the config.json
```json
{
  "token" : "token"
}
```

##### User credentials
To use your GitHub user credentials, add the following:
```json
{
  "username" : "username",
  "password" : "password
}
```

#### Dependencies
This script uses [PyGithub](https://github.com/PyGithub/PyGithub)

Install PyGithub by running `$ pip install PyGithub`
