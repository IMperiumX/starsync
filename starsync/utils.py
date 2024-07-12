from timeit import default_timer

import requests

from .constants import *


def timer(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        func(*args, **kwargs)
        elapsed = default_timer() - start
        print(f"Elapsed Time: {elapsed:.2f} seconds")

    return wrapper


def write_to_file(repos, schema_attr="full_name"):
    with open("repos.txt", "w") as f:
        for repo in repos:
            f.write(repo[schema_attr] + "\n")


def read_from_file(filename=FILE_PATH):
    with open(filename, "r") as f:
        return f.read().splitlines()


def data_persestance(repos):
    write_to_file(repos)
    repos = read_from_file()
    return repos


def list_starred_repos():
    return requests.get(STARRED_ENDPONT, headers=HEADERS)


@timer
def unstar_repo(repo):
    if isinstance(repo, list):
        _handle_unstar_repos(repo)
    URL = URL_TEMPLATE.substitute(repo=repo)
    r = requests.delete(URL, headers=HEADERS)
    return f">{r.status_code} - {repo}"


def _handle_unstar_repos(repos):
    for repo in repos:
        r = requests.delete(URL_TEMPLATE.safe_substitute(repo=repo), headers=HEADERS)
        print(f">{r.status_code} - {repo}")
    return "Done"


# used in  async function
def fetch(session, repo):
    start = default_timer()
    URL = URL_TEMPLATE.substitute(repo=repo)
    response = session.delete(URL, headers=HEADERS)
    total = default_timer() - start
    return f"{response.status_code} {total:.2f} {URL}"
