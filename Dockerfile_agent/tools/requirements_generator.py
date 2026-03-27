from utils.llm import get_llm


def clean_output(text: str) -> str:
    text = text.strip()

    # Remove markdown blocks
    if "```" in text:
        text = text.split("```")[1]

    lines = text.split("\n")

    # Keep only valid lines (no spaces → likely package names)
    cleaned = [line.strip() for line in lines if line.strip() and " " not in line]

    return "\n".join(cleaned)


def generate_requirements(user_input: str) -> str:
    llm = get_llm()

    prompt = (
        "Generate requirements.txt for this app.\n\n"
        f"{user_input}\n\n"
        "Only package names. No explanation."
    )

    response = llm.invoke(prompt)

    cleaned_resp = clean_output(response.content)

    return cleaned_resp