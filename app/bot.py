from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import logging
from aiogram.types import InputFile
from app.sentiment import analyze_sentiment
from app.utils import create_pie_chart
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.reply("Привет! Отправь ссылку на видео, и я проанализирую комментарии.")

@dp.message()
async def analyze_comments(message: Message):
    user_input = message.text
    try:
        video_id = user_input.split("v=")[-1]
        comments = await get_comments_from_youtube(video_id)

        sentiment_counts = {"позитивное": 0, "нейтральное": 0, "негативное": 0}

        for comment in comments:
            sentiment = await analyze_sentiment(comment)
            sentiment_counts[sentiment] += 1

        create_pie_chart(sentiment_counts)

        await message.reply_photo(photo=InputFile("sentiment_pie_chart.png"))
    except Exception as e:
        logging.error(f"Ошибка при анализе комментариев: {e}")
        await message.reply("Произошла ошибка при анализе комментариев. Попробуйте еще раз.")

async def get_comments_from_youtube(video_id: str):
    from googleapiclient.discovery import build
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=youtube_api_key)

    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments