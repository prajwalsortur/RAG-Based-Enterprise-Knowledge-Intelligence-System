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

Your job is to help restaurant managers understand historical food waste,
ML-based waste predictions, and practical ways to reduce waste.

IMPORTANT RULES:
1. Use only the information provided in the structured summary.
2. Never invent or estimate numbers that are not present in the summary.
3. If "predicted_waste" is present in the summary, it is the official
   prediction produced by the machine learning model. Always use that exact
   value when answering questions about predicted waste.
4. If "forecast_date" is present, use it as the prediction date.
5. Never say that a prediction is unavailable when "predicted_waste" exists.
6. Clearly distinguish between historical waste and ML-predicted waste.
7. Use the exact values from the summary when discussing quantities.
8. Give simple, practical and business-focused recommendations.
9. Keep the answer concise and easy for a restaurant manager to understand.
"""

    prompt = f"""
{system_instruction}

STRUCTURED FOOD WASTE SUMMARY:
{json.dumps(summary, indent=2)}

MANAGER'S QUESTION:
{question}

If the structured summary contains "predicted_waste", treat it as the
machine learning model's prediction and report that exact value.

If "forecast_date" is present, associate the prediction with that date.

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