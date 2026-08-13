import os
import json

from dotenv import load_dotenv
from google import genai


# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(question, summary):

    system_instruction = """
You are a restaurant food-waste analytics assistant.

Your job is to help restaurant managers understand food waste.

IMPORTANT RULES:
1. Use only the information provided in the structured summary.
2. Do not invent numbers.
3. If the summary does not contain enough information, clearly say so.
4. Give simple and practical recommendations.
5. Keep the answer concise and business-focused.
"""

    prompt = f"""
{system_instruction}

STRUCTURED FOOD WASTE SUMMARY:
{json.dumps(summary, indent=2)}

MANAGER'S QUESTION:
{question}

Answer the manager using only the structured summary.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# Test the GenAI layer
if __name__ == "__main__":

    with open("summary.json", "r") as file:
        summary = json.load(file)

    question = "What are the main food waste problems in this restaurant?"

    answer = ask_gemini(question, summary)

    print("========================================")
    print("GENAI RESPONSE")
    print("========================================")
    print(answer)