import os

def write_files(requirements: str, dockerfile: str, path: str) -> str:
    os.makedirs(path, exist_ok=True)

    req_path = os.path.join(path, "requirements.txt")
    docker_path = os.path.join(path, "Dockerfile")

    with open(req_path, "w") as f:
        f.write(requirements)

    with open(docker_path, "w") as f:
        f.write(dockerfile)

    return f"Files saved at {os.path.abspath(path)}"