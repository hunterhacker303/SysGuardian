import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3",
        "prompt": "Explain high CPU usage",
        "stream": False
    },
    timeout=60
)

data = response.json()
print(data["response"])