import asyncio
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎁 Claim Bonus 100% + 100 Free Spins",
            url="https://go.777vault.partners/visit/?bta=35054&nci=5352"
        )]
    ])
    await message.answer(
        "👋 <b>Hey! Welcome aboard!</b>\n\n"
        "We're thrilled to have you here! 🎰\n\n"
        "As a new player, you're entitled to an amazing <b>Welcome Casino Bonus — 100% up to €500 + 100 Free Spins!</b> 🎁\n\n"
        "Double your bankroll and spin the reels for free from day one — don't miss out!\n\n"
        "👇 Hit the button below and claim your bonus right now:\n\n"
        "🎰 <a href='https://go.777vault.partners/visit/?bta=35054&nci=5352'>777vault</a> — play and win!",
        parse_mode="HTML",
        reply_markup=kb
    )

async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
