import streamlit as st
from tools.dockerfile_generator import generate_dockerfile
from tools.requirements_generator import generate_requirements
from tools.docker_builder import build_docker_image
from utils.image_utils import norm_image_name

st.title("🤖 AI Dockerfile Agent")

user_input = st.text_area("Describe your Python app")

image_name = st.text_input("Enter image name (e.g. user/app:tag)")

if st.button("Generate & Build"):
    if user_input:
        st.write("### Generating requirements.txt...")
        requirements = generate_requirements(user_input)
        st.code(requirements)

        st.write("### Generating Dockerfile...")
        dockerfile = generate_dockerfile(user_input)
        st.code(dockerfile)

        image_name = norm_image_name(image_name)

        st.write("### Building Docker Image...")
        result = build_docker_image(".", image_name)
        st.text(result)
    else:
        st.warning("Please enter app description")