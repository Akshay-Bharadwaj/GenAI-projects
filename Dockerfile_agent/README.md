# 🤖 AI Dockerfile Agent

An AI-powered tool that converts application requirements into a working Docker image.

## 🚀 Features

- Generate `requirements.txt` from natural language
- Generate production-ready `Dockerfile`
- Clean LLM outputs for system compatibility
- Build Docker image automatically
- Streamlit UI for interaction

## 🧱 Tech Stack

- Python
- Groq (LLM API)
- Streamlit
- Docker

## ⚙️ How It Works

1. User provides application description
2. LLM generates dependencies
3. LLM generates Dockerfile
4. Outputs are cleaned and validated
5. Docker image is built locally

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Build Docker (via app)

The application automatically builds Docker images using generated files.

## 🔮 Future Improvements
Convert into AI agent with tool-based reasoning
Add multi-language support
Improve error handling and validation
Deploy on cloud (AWS/GCP/Azure)

## 📌 Author

Akshay Bharadwaj
