import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

TOKEN = "8883366446:AAH4bFH3UxIxP5mVoJ1dkGYZjRwz8Tvs7EA"

bot = Bot(token="8883366446:AAH4bFH3UxIxP5mVoJ1dkGYZjRwz8Tvs7EA")
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📢 Kanal"), KeyboardButton(text="🎁 Konkurs")],
        [KeyboardButton(text="📰 Yangiliklar"), KeyboardButton(text="💬 Admin")],
        [KeyboardButton(text="ℹ️ Bot haqida")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "⚽ FC PRO UZ botiga xush kelibsiz!",
        reply_markup=menu
    )

@dp.message(F.text == "📢 Kanal")
async def channel(message: Message):
    await message.answer("📢 Kanal: https://t.me/FC_PRO_UZ")

@dp.message(F.text == "🎁 Konkurs")
async def contest(message: Message):
    await message.answer(
        "🎁 Konkurs bu kanalda bo'ladi:https://t.me/FC_PRO_UZ!" \
        "bu yerda aktiv bo'ling konkurslar tez bo'ladi"
    )

@dp.message(F.text == "📰 Yangiliklar")
async def news(message: Message):
    await message.answer(
        "📰 FC Mobile yangiliklarni shu kanaldan topasiz:https://t.me/FC_PRO_UZ."
    )

@dp.message(F.text == "💬 Admin")
async def admin(message: Message):
    await message.answer(
        "👤 Admin:\n@N_57001\n@m23041956"
    )

@dp.message(F.text == "ℹ️ Bot haqida")
async def info(message: Message):
    await message.answer(
        "🤖 FC PRO UZ rasmiy boti.\n"
        "Yangiliklar, konkurslar va foydali ma'lumotlar uchun xizmat qiladi."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())