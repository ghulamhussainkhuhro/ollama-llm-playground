import requests

# Ollama REST API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"

# Helper function to send a prompt
def ollama_chat(model, messages, max_tokens=200, temperature=0.1):
    data = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    return response.json()

# # Example usage
if __name__ == "__main__":
    text_to_summarize = (
        "Ollama is a platform that allows users to run and manage large language models (LLMs) "
        "locally on their own hardware. It provides an easy-to-use interface for deploying, "
        "interacting with, and fine-tuning various LLMs without needing extensive technical knowledge."
    )
    model_name = "llama3.2:latest"
    messages = [
        {"role": "system", "content": "Summarize the following text in 4 words."},
        {"role": "user", "content": text_to_summarize}
    ]

    response = ollama_chat(model_name, messages)
    answer = response["choices"][0]["message"]["content"]
    print("Summary:", answer)