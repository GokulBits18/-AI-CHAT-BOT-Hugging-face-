import streamlit as st
from transformers import pipeline

st.title("AI Chatbot")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    )

pipe = load_model()

# System prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and briefly.
If you do not know something, say you do not know.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user = st.chat_input("Type your message")

if user:

    st.session_state.messages.append(
        {"role": "user", "content": user}
    )

    with st.chat_message("user"):
        st.write(user)

    # Build prompt
    prompt = f"<|system|>\n{SYSTEM_PROMPT}\n"

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            prompt += f"<|user|>\n{msg['content']}\n"
        else:
            prompt += f"<|assistant|>\n{msg['content']}\n"

    prompt += "<|assistant|>\n"

    result = pipe(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    output = result[0]["generated_text"]

    response = output.split("<|assistant|>")[-1].strip()

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)