# AI Web Assistant (Groq + DuckDuckGo)

A small Python AI chatbot that uses **Groq** for natural language processing and **DuckDuckGo** for web search.  
The assistant can answer user questions and perform simple calculations.

---
## Features

- Chatbot powered by Groq LLM
- Search the web via DuckDuckGo
- Perform basic math calculations
- Easy to run locally with Python

---

## Setup Instructions

### 1. Get a Groq API Key

1. Go to [Groq Developer Portal](https://www.groq.com/) and sign up for a free account.  
2. Generate a free **Groq API key** from your account dashboard.  
3. Copy the API key and paste it inside the quotes in the .env file.

---

### 2. Set up a Python virtual environment (recommended)
1. Open your terminal and navigate to the project folder.
2. Run the following to create a virtual environment:
    ```bash
    python -m venv .venv (or py -m venv .venv)

3. Activate the virtual environment by running:
    ```bash
    .venv\Scripts\activate (on Windows)
    or
    source .venv/bin/activate (on Linux and MacOS)

### 3. Install dependancies
1. Once your virtual environment is active, install the required packages:
    ```bash
    pip install -r requirements.txt

### 4. Run the chatbot
    ```bash
    python main.py








