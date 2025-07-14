# ATS Resume Evaluator with Local LLM (DeepSeek & Ollama)

This project is a web app that evaluates job candidates' resumes against job descriptions using a local Large Language Model (LLM).  
It uses [DeepSeek](https://ollama.com/models/deepseek) running via [Ollama](https://ollama.com) and [Streamlit](https://streamlit.io/) for the user interface.

---

##  Features

- Extracts text from uploaded PDF resumes
- Compares resumes to job descriptions using DeepSeek LLM
- Provides ATS-style evaluation and keyword match percentage
- Runs fully locally — no API keys or cloud usage
- Displays the model’s reasoning if needed

---

##  Tech Stack

- Python 3.10+
- Streamlit (Web UI)
- PyMuPDF (PDF text extraction)
- Ollama (for local LLM inference)
- DeepSeek R1 model (`deepseek-r1:1.5b`)

---

##  Getting Started

To run this app on your local machine, follow these steps:

1. **Install Ollama**  
   Download and install Ollama from the official website:  
   [https://ollama.com/download](https://ollama.com/download)

2. **Download the DeepSeek model**  
   Open a terminal or command prompt and run:
   ```bash
   ollama pull deepseek-r1:1.5b
3. **Clone this repository**
4. **Create and activate a virtual environment**
5. **Install the project dependencies**
   Open a terminal or command prompt and run:
   ```bash
   pip install -r requirements.txt
6. **Start the Streamlit app**
   Open a terminal or command prompt and run:
   ```bash
   streamlit run app.py
