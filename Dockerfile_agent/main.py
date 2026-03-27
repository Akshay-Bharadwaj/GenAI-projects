from tools.docker_builder import build_docker_image
from tools.dockerfile_generator import generate_dockerfile
from tools.file_writer import write_files
from tools.requirements_generator import generate_requirements
from utils.image_utils import norm_image_name


def run_agent():
    user_input = input("Describe your Python app: ")
    path = input("Enter path (default = current dir): ") or "."
    image_name = input("Enter image name (e.g. user/app:tag): ")

    image_name = norm_image_name(image_name)

    print(f"Generating requirements.txt ...\n")
    requirements = generate_requirements(user_input)

    print(f"Generating Dockerfile ...\n")
    dockerfile = generate_dockerfile(user_input)

    print("Saving the files ...")
    print(write_files(requirements, dockerfile, path))

    print(f"Building Docker image {image_name} ...\n")
    print(build_docker_image(path, image_name))


if __name__ == "__main__":
    run_agent()
