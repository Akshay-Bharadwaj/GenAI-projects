from utils.llm import get_llm

def clean_output(text: str) -> str:
    lines = text.strip().split("\n")

    # Remove first line if it starts with ```
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]

    # Remove last line if it starts with ```
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]

    return "\n".join(lines).strip()

def generate_dockerfile(user_input: str) -> str:
    llm = get_llm()

    prompt = (
        "Create a Dockerfile for this Python application.\n\n"
    f"{user_input}\n\n"
    "Use python:3.10-slim.\n"
    "Use WORKDIR /app.\n"
    "Install from requirements.txt.\n"
    "Expose correct port.\n"
    "IMPORTANT: Return ONLY Dockerfile. No explanation. No markdown."
    )

    response = llm.invoke(prompt)

    cleaned_resp = clean_output(response.content)

    return cleaned_resp

