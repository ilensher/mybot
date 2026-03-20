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
```

---

## ШАГ 3 — Сохрани изменения в GitHub

**1.** После того как вставил код — найди зелёную кнопку **"Commit changes"** (в правом верхнем углу редактора)

**2.** Появится окошко. В поле **"Commit message"** напиши:
```
Add source tracking
```

**3.** Нажми зелёную кнопку **"Commit changes"**

**4.** GitHub сохранит файл и автоматически отправит обновление в Railway

---

## ШАГ 4 — Проверь что Railway задеплоил обновление

**1.** Зайди на **railway.app** → твой проект **mybot**

**2.** Подожди 1–2 минуты — должен появиться новый деплой

**3.** Статус должен стать **ACTIVE / Deployment successful** — как был раньше

---

## ШАГ 5 — Проверь что всё работает

Теперь у тебя есть два типа ссылок на бота:

**Обычная ссылка (без источника):**
```
t.me/ИМЯ_ТВОЕГО_БОТА
```
Пользователь получит ссылку с `sub1=organic`

**Ссылка для Kick стримера John:**
```
t.me/ИМЯ_ТВОЕГО_БОТА?start=kick_john
```
Пользователь получит ссылку с `sub1=kick_john`

**Ссылка для Telegram канала:**
```
t.me/ИМЯ_ТВОЕГО_БОТА?start=tg_channel1
```
Пользователь получит ссылку с `sub1=tg_channel1`

---

## ШАГ 6 — Проверь в Telegram

**1.** Открой своего бота в Telegram

**2.** Перейди по ссылке:
```
t.me/ИМЯ_БОТА?start=test_source
