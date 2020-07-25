#### Description
Create and initialize a GitHub Repo in the current folder.

### How to
To run the script globally, you can symlink `cli.py` to your `/usr/local/bin`. You might have to add executable permissions to `cli.py` and `git-init.py`.
```
$ chmod +x cli.py git-init.py
```

Run `$ ln -s /path/to/script/cli.py /usr/local/bin/your-name-for-the-command`. Sudo might be necessary.

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
