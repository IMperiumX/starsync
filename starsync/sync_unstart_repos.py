"""
unstart all repos in your github account
"""
from string import Template
from timeit import default_timer

from .utils import data_persestance, list_starred_repos, unstar_repo


def unstar_repos_async():
    start = default_timer()

    response = list_starred_repos()
    repos = data_persestance(response.json())
    unstar_repo(repos)

    total = default_timer() - start
    return f"{response.status_code} {total:.2f}"


if __name__ == "__main__":
    start = default_timer()
    unstar_repos_async()
    elapsed = default_timer() - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")
