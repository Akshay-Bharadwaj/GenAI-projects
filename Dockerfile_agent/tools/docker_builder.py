import subprocess


def build_docker_image(path: str, image_name: str) -> str:
    command = ["docker", "build", "-t", image_name, path]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        return f"[SUCCESS] Image built: {image_name}"

    return f"[ERROR]\n{result.stderr}"