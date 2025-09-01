import requests
import json

# Ollama REST API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"

# Request payload
data = {
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Explain REST API in 2 sentences."}
    ],
    "max_tokens": 200,
    "temperature": 0.7,
    "stream": True  # Enable streaming
}

with requests.post(OLLAMA_API_URL, json=data, stream=True) as response:
    if response.status_code == 200:
        print("Assistant:", end=" ", flush=True)
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")

                # The server sends "data: ..." lines
                if decoded_line.startswith("data: "):
                    payload = decoded_line[len("data: "):]

                    if payload == "[DONE]":
                        break

                    try:
                        event = json.loads(payload)
                        delta = event["choices"][0]["delta"].get("content")
                        if delta:
                            print(delta, end="", flush=True)
                    except Exception:
                        pass
        print()  # final newline
    else:
        print(f"Error: {response.status_code} - {response.text}")
