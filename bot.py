# bot.py — ваш продающий бот (полностью рабочий)

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import asyncio

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# СЮДА ВСТАВЬТЕ СВОЙ ТОКЕН ОТ @BotFather
TOKEN = "8444877639:AAGCSaXaxYPtmBGAIlwEUkJJvQRtwUj-4HQ"   # ←← замените!
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Главное меню
@router.message(Command("start"))
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что это такое?", callback_data="what")],
        [InlineKeyboardButton(text="Сколько стоит?", callback_data="price")],
        [InlineKeyboardButton(text="Что я получу?", callback_data="result")],
        [InlineKeyboardButton(text="Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="Оплатить прямо сейчас", callback_data="pay")]
    ])
    
    await message.answer(
        "Привет! 👋\n\nЯ помогу тебе узнать всё о курсе/услуге и сразу купить, если захочешь.\n\n"
        "Выбери интересующий пункт:",
        reply_markup=keyboard
    )

# Ответы на кнопки (быстро поменяете под себя)
@router.callback_query(F.data == "what")
async def what(callback: CallbackQuery):
    await callback.message.answer("🔥 Здесь подробное описание вашего продукта...\n\n"
                                  "Пиши /start — вернёшься в меню")
    await callback.answer()

@router.callback_query(F.data == "price")
async def price(callback: CallbackQuery):
    await callback.message.answer("💰 Цены:\n\n"
                                  "• Базовый тариф — 4 990 ₽\n"
                                  "• Премиум — 9 990 ₽\n"
                                  "• VIP (с проверкой ДЗ) — 19 990 ₽\n\n"
                                  "Пиши /start — вернёшься в меню")
    await callback.answer()

@router.callback_query(F.data == "result")
async def result(callback: CallbackQuery):
    await callback.message.answer("✅ Что ты получишь:\n\n"
                                  "• 8 недель обучения\n"
                                  "• 50+ видео-уроков\n"
                                  "• Закрытый чат с кураторами\n"
                                  "• Сертификат\n"
                                  "• И главное — результат!\n\n"
                                  "Пиши /start — вернёшься в меню")
    await callback.answer()

@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):
    await callback.message.answer("❓ Частые вопросы:\n\n"
                                  "— Нужен ли опыт? Нет, с нуля\n"
                                  "— Есть рассрочка? Да, от 416 ₽/мес\n"
                                  "— Вернёте деньги? Да, 14 дней гарантия\n"
                                  "— Сколько времени в неделю? 5–7 часов\n\n"
                                  "Пиши /start — вернёшься в меню")
    await callback.answer()

# Кнопка оплаты
@router.callback_query(F.data == "pay")
async def pay(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить 9 990 ₽ (премиум)", url="https://example.com/pay")],
        [InlineKeyboardButton(text="Выбрать другой тариф", callback_data="price")]
    ])
    await callback.message.answer(
        "Выбери тариф и оплати за 10 секунд 👇\n\n"
        "После оплаты доступ придёт автоматически в течение 1–2 минут",
        reply_markup=keyboard
    )
    await callback.answer()

async def main():
    dp.include_router(router)
    print("Бот запущен и работает 24/7!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())