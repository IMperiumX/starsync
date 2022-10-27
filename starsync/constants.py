# Environment variables

import os

get_env = os.environ.get
APIKEY = get_env("APIKEY")


# String Templates

from string import Template

URL_TEMPLATE = Template("https://api.github.com/user/starred/$repo")

HEADERS = headers = {
    "Authorization": f"Bearer {APIKEY}",
    "Accept": "application/vnd.github+json",
}

# API Endpoints

STARRED_ENDPONT = "https://api.github.com/user/starred"

# files realted

from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent
FILE_NAME = "repos.txt"
FILE_PATH = PROJECT_PATH / FILE_NAME
