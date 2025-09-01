import requests
import json

# Ollama REST API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"

# Helper function to send a prompt
def ollama_chat(model, messages, max_tokens=200, temperature=0.7):
    data = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    return response.json()

# # Example usage
# if __name__ == "__main__":
#     model_name = "llama3.2:latest"
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello, how are you?"}
#     ]
    
#     response = ollama_chat(model_name, messages)
#     print(json.dumps(response, indent=2))

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain REST API in 2 sentences."}
]

response = ollama_chat("llama3.2", messages)
print(json.dumps(response, indent=2))

# extracting just answer
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain REST API in 2 sentences."}
]

response = ollama_chat("llama3.2", messages)
answer = response["choices"][0]["message"]["content"]
print("Assistant:", answer)
# Note: Ensure that the Ollama server is running and the specified model is available.