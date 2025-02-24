from fastapi import FastAPI
import logging
import asyncio
from app.bot import dp, bot
import threading

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API работает"}

async def run_bot():
    await dp.start_polling(bot)

def start_bot():
    asyncio.run(run_bot())

if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)