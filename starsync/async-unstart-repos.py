import asyncio

import requests

from .utils import fetch, read_from_file, timer


@timer
async def unstar_repos_async():
    with requests.Session() as session:
        loop = asyncio.get_event_loop()

        repos = read_from_file()

        tasks = [loop.run_in_executor(None, fetch, session, repo) for repo in repos]

        for response in await asyncio.gather(*tasks):
            print(response)


if __name__ == "__main__":
    unstar_repos_async()
