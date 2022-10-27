import asyncio
from timeit import default_timer

import requests

from .utils import fetch, read_from_file


async def unstar_repos_async():
    with requests.Session() as session:
        loop = asyncio.get_event_loop()

        # Take each URL in the list
        # make an async task from it that uses
        # `fetch` to get the data from the URL
        # and start the task running in the event loop

        repos = read_from_file()

        tasks = [loop.run_in_executor(None, fetch, session, repo) for repo in repos]

        # Gather all the tasks from the event loop
        # once they finish running.
        # (This command blocks).

        for response in await asyncio.gather(*tasks):
            print(response)


if __name__ == "__main__":
    start = default_timer()
    asyncio.run(unstar_repos_async())
    elapsed = default_timer() - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")
