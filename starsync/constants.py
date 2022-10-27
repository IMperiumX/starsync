APIKEY = "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"

URL_TEMPLATE = template = Template("https://api.github.com/user/starred/$repo")

HEADERS = headers = {
    "Authorization": f"Bearer {APIKEY}",
    "Accept": "application/vnd.github+json",
}

STARRED_ENDPONT = "https://api.github.com/user/starred"
