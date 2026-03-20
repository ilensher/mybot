import asyncio
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.types import BotCommand

router = Router()

# База пользователей — храним в памяти (простое решение без БД)
users = {}

@router.message(CommandStart())
async def start(message: Message):

    # Получаем параметр из ссылки ?start=ПАРАМЕТР
    args = message.text.split()
    source = args[1] if len(args) > 1 else "organic"

    # Сохраняем пользователя и его источник
    user_id = message.from_user.id
    users[user_id] = {"source": source}

    # Подставляем source в реф.ссылку как sub1
    ref_url = f"https://go.777vault.partners/visit/?bta=35054&nci=5352&sub1={source}"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎁 Claim Bonus 100% + 100 Free Spins",
            url=ref_url
        )]
    ])

    await message.answer(
        "👋 <b>Hey! Welcome aboard!</b>\n\n"
        "We're thrilled to have you here! 🎰\n\n"
        "As a new player, you're entitled to an amazing <b>Welcome Casino Bonus — 100% up to €500 + 100 Free Spins!</b> 🎁\n\n"
        "Double your bankroll and spin the reels for free from day one — don't miss out!\n\n"
        "👇 Hit the button below and claim your bonus right now:\n\n"
        "🎰 <a href='" + ref_url + "'>777vault</a> — play and win!",
        parse_mode="HTML",
        reply_markup=kb
    )

async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
