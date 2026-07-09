# TinyLlama AI Chatbot

A lightweight AI chatbot built with **Python**, **Streamlit**, and **Hugging Face Transformers**. The application uses the **TinyLlama-1.1B-Chat** language model to provide real-time conversational responses through an interactive chat interface.

---

#  Project Overview

TinyLlama AI Chatbot is a conversational AI application that enables users to interact with a locally loaded Large Language Model (LLM). Built using Streamlit and the Hugging Face Transformers library, the chatbot generates intelligent responses while maintaining conversation history throughout the session.

The project demonstrates how open-source language models can be integrated into web applications for offline or local AI-powered conversations.

---

#  Features

- AI-powered conversational chatbot
- Interactive Streamlit chat interface
- Local inference using TinyLlama
- Conversation history with session state
- Cached model loading for improved performance
- Custom system prompt for response control
- Fast and lightweight deployment

---

#  Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- TinyLlama
- PyTorch
- Natural Language Processing (NLP)
- Large Language Models (LLMs)

---

#  How the System Works

The application follows these steps:

1. Load the TinyLlama language model.
2. Display the chat interface.
3. User enters a message.
4. The application builds a prompt containing the system instruction and conversation history.
5. TinyLlama generates a response.
6. The response is displayed and stored for future interactions.

---

#  Project Structure

```
TinyLlama-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

---

#  Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/tinyllama-chatbot.git

cd tinyllama-chatbot
```

---

## Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit transformers torch
```

---

#  Running the Project

Launch the Streamlit application:

```bash
streamlit run app.py
```

The chatbot will open automatically in your web browser.

---

#  AI Model

**Model Used**

```
TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

TinyLlama is a compact open-source Large Language Model optimized for conversational AI tasks. It provides efficient text generation while requiring fewer computational resources than larger models.

---

#  Code Workflow

### Load the Model

```python
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)
```

### User Input

Users enter messages through the Streamlit chat interface.

### Prompt Construction

The application combines:

- System prompt
- Previous conversation history
- Current user message

to create the input prompt for the model.

### Generate Response

```python
result = pipe(
    prompt,
    max_new_tokens=200,
    temperature=0.7,
    top_p=0.9
)
```

### Display Response

The generated reply is displayed and saved in the session history.

---

#  Example Conversation

### User

```
What is Artificial Intelligence?
```

### AI

```
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and understanding language.
```

---

#  Applications

- AI Virtual Assistant
- Educational Chatbot
- Coding Assistant
- Personal Productivity
- Question Answering
- Research Support
- NLP Learning Projects
- Offline AI Applications

---

#  Future Improvements

- Multi-turn memory
- Voice input and speech output
- File upload and analysis
- Streaming AI responses
- Chat export (PDF/TXT)
- Dark mode UI
- Multiple LLM support
- Cloud deployment

---

#  Learning Outcomes

This project demonstrates:

- Large Language Models (LLMs)
- Hugging Face Transformers
- Streamlit chat applications
- Text generation pipelines
- Prompt engineering
- Session state management
- Local AI model deployment

---


#  Author

Developed using Python, Streamlit, Hugging Face Transformers, and TinyLlama to demonstrate a lightweight AI chatbot capable of generating conversational responses locally.
