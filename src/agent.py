import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1"
)


def run_agent(user_input):
    response = client.chat.completions.create(
        model="gpt-oss:20b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return response.choices[0].message.content


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