def write_to_file(repos, schema_attr="full_name"):
    with open("repos.txt", "w") as f:
        for repo in repos:
            f.write(repo[schema_attr] + "\n")


def read_from_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()
