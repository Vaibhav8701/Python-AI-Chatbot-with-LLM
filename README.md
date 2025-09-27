

# Project Overview: Python AI Chatbot with LLM
# 1. Goal

Build a simple AI chatbot using Python.

It answers common questions about Python, NumPy, and Pandas (FAQ).

If the answer isn’t in the FAQ, it uses an LLM (OpenAI GPT) to generate the response.

# 2. Tech Stack

Python 3.11 (core language you know).

OpenAI Python library (to connect with GPT model).

Dictionary (FAQ) → Mini RAG (Retrieval-Augmented Generation).

# 3. Workflow

User enters a question in the terminal.

Chatbot first checks the FAQ dictionary (predefined answers).

If question is found → reply directly.

If not found → send the question to OpenAI LLM.

LLM generates a smart answer.

Chatbot prints the reply back to the user.

# 4: Key Features

Mini-RAG implementation (Retrieve → Generate)

Fallback to LLM for unknown questions

Simple, clean, and extendable project

Can integrate with CSV / Pandas for larger FAQs
