import requests

# Ollama REST API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"

# Helper function to send a prompt
data = {
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Explain REST API in 2 sentences."}
    ],
    "max_tokens": 200,
    "temperature": 0.7,
    "stream": True  # Enable streaming responses
}

with requests.post(OLLAMA_API_URL, json=data, stream=True) as response:
    if response.status_code == 200:
        print("Streaming response:")
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(decoded_line)
    else:
        print(f"Error: {response.status_code} - {response.text}")