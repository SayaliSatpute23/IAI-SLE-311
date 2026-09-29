import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OLLAMA_API_KEY")
URL = "https://ollama.com/v1/chat/completions"

def run_agent(user_input):
    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-oss:20b",
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main():
    print("===== BASIC AI AGENT =====")
    print("Type 'exit' to stop.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        answer = run_agent(user_input)
        print("Agent:", answer)

if __name__ == "__main__":
    main()
