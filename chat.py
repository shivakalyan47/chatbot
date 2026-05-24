"""
Install dependencies:
pip install google-genai python-dotenv
"""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """you are a teacher in bms college, you are teaching a student who is in 1st year of engineering, you have to teach him about the subject of engineering graphics, you have to teach him in a very simple way, you have to give him examples and also you have to give him some exercises to practice.
"""

def get_gemini_response(user_input: str, chat_history: list) -> str:
    """
    Sends the user input along with existing chat history to Gemini,
    appends user and model contents to chat_history in-place,
    and returns the bot's response text.
    """
    # Add user message
    chat_history.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input)
            ]
        )
    )

    # Generate response
    response = client.models.generate_content(
    model="gemini-2.5-flash",  # 1. Switch to stable, high-speed model
    contents=chat_history[-10:], # 2. Only send the last 10 messages to control history size
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.7,
        top_p=0.95,
        top_k=64,
        max_output_tokens=1524,  # 3. Limit maximum length of one reply (e.g. ~1000 words)
        response_mime_type="text/plain",
        # 4. REMOVED thinking_config to get instant, real-time responses!
    )
)

    model_response = response.text

    # Save bot response
    chat_history.append(
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=model_response)
            ]
        )
    )

    return model_response


if __name__ == "__main__":
    # Store chat history for interactive command-line mode
    chat_history = []

    print("Bot: Hello, how can I help you?")
    print()

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nBot: Goodbye!")
            break

        print()

        try:
            model_response = get_gemini_response(user_input, chat_history)
            print(f"Bot: {model_response}")
        except Exception as e:
            print(f"Error: {e}")
        print()