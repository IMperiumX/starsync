"""
unstart all repos in your github account
"""
from timeit import default_timer

from .utils import data_persestance, list_starred_repos, unstar_repo


def unstar_repos_sync():
    start = default_timer()

    response = list_starred_repos()
    repos = data_persestance(response.json())
    unstar_repo(repos)

    total = default_timer() - start
    return f"{response.status_code} {total:.2f}"


if __name__ == "__main__":
    unstar_repos_sync()
