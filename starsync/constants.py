# Environment variables

import os
from pathlib import Path
from string import Template

get_env = os.environ.get


APIKEY = get_env("APIKEY")


# String Templates

URL_TEMPLATE = Template("https://api.github.com/user/starred/$repo")

HEADERS = headers = {
    "Authorization": f"Bearer {APIKEY}",
    "Accept": "application/vnd.github+json",
}

# API Endpoints

STARRED_ENDPONT = "https://api.github.com/user/starred"

# files realted

PROJECT_PATH = Path(__file__).resolve().parent
FILE_NAME = "repos.txt"
FILE_PATH = PROJECT_PATH / FILE_NAME

__all__ = [
    "get_env",
    "APIKEY",
    "URL_TEMPLATE",
    "HEADERS",
    "STARRED_ENDPONT",
    "FILE_PATH",
]
