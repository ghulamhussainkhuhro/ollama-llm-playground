import requests

# Ollama REST API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"
# Helper function to send a prompt
def ollama_chat(model, messages, max_tokens=200, temperature= 0.7):
    data={
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    return response.json()

# Example usage 
if __name__ == "__main__":
    sentiment_text = (
        "I had a wonderful experience at the restaurant. The food was delicious and the service was excellent!"
    )
    model_name = "llama3.2:latest"
    messages = [
        {"role": "system", "content": "Analyze the sentiment of the following text as Positive, Negative, or Neutral."},
        {"role": "user", "content": sentiment_text}
    ]
    response = ollama_chat(model_name, messages)
    answer = response["choices"][0]["message"]["content"]
    print("Sentiment Analysis:", answer)
    