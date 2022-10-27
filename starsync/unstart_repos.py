"""
unstart all repos in your github account
"""
from string import Template
from timeit import default_timer

import requests

from .constants import *
from .utils import read_from_file, write_to_file


def list_starred_repos():
    return requests.get(STARRED_ENDPONT, headers=HEADERS)


def _handle_unstar_repos(repos):
    for repo in repos:
        r = requests.delete(URL_TEMPLATE.substitute(repo=repo), headers=HEADERS)
        print(f">{r.status_code} - {repo}")
    return "Done"


def unstar_repo(repo):
    if isinstance(repo, list):
        _handle_unstar_repos(repo)
    URL = URL_TEMPLATE.substitute(repo=repo)
    r = requests.delete(URL, headers=HEADERS)
    return f">{r.status_code} - {repo}"


def unstar_repos_async():
    start = default_timer()

    response = list_starred_repos()
    repos = response.json()
    write_to_file(repos)
    repos = read_from_file()
    unstar_repo(repos)
    total = default_timer() - start
    return f"{response.status_code} {total:.2f}"


if __name__ == "__main__":
    start = default_timer()
    unstar_repos_async()
    elapsed = default_timer() - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")
