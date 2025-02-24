import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


async def analyze_sentiment(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — помощник для анализа настроений текста."},
            {"role": "user",
             "content": f"Определи настроение следующего текста (позитивное, негативное, нейтральное):\n{text}"}
        ],
        max_tokens=10,
        temperature=0.5
    )

    sentiment = response["choices"][0]["message"]["content"].strip().lower()

    if "позитив" in sentiment:
        return "позитивное"
    elif "негатив" in sentiment:
        return "негативное"
    return "нейтральное"
