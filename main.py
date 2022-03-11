import types
import buttons
import aiogram
from aiogram import Bot, Dispatcher, executor,types
import logging
import wikipedia
from  aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

logging.basicConfig(level=logging.INFO)


bot = Bot(token='5119889178:AAHEY-yeeA9_Es4nq0fgrg3R4M_sNlSzr94')
dp = Dispatcher(bot)

#strat btn
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Assalomu alekum {message.from_user.first_name}!\n\nWikipedia botga hush kelibsiz!!!\n<b>Tilni tanlang</b>👇", reply_markup=buttons.inl, parse_mode='html')

@dp.callback_query_handler()
async def set_lan(call: types.CallbackQuery):
    text = f"Til tanlandi!\n<b>Nima ma'lumot kerak?"
    if call.data == 'uz':
        wikipedia.set_lang('uz')
        await call.answer("Til tanlandi✅")
        await call.message.edit_text(text,parse_mode='html')

    elif call.data == 'ru':
        wikipedia.set_lang('ru')
        await call.answer("Til tanlandi✅")
        await call.message.edit_text(text, parse_mode='html')
    elif wikipedia.set_lang('en'):
        wikipedia.set_lang('en')
        await call.answer("Til tanlandi✅")
        await call.message.edit_text(text, parse_mode='html')


@dp.message_handler(content_types=['text'])
async def send(message: types.Message):
    d = 0
    if message.text == "Tilni o'zgartirish🔁":
        await message.answer("Tilni o'zgartirish👇👇👇", reply_markup=buttons.inl)
        d = 1
    if d == 0:
        try:
            await message.answer(wikipedia.summary(message.text),parse_mode='html', reply_markup=buttons.qayta)
        except: await message.answer('Bunday malumot topilmadi yoki tilni xato kiritgansiz!!!')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
