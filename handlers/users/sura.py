from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db, dp
from aiogram import types
from states.full import my_State
from keyboards.default.start import main_markup, back_button, main_menu_button
from aiogram.dispatcher import FSMContext
import json
import requests


@dp.message_handler(state=my_State.Suralar)
async def send_sura(message: types.Message, state: FSMContext):
    r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json").json()
    main_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    sura_name = []
    for sura in r['chapters']:
        sura_name.append(sura['name'])

    for i in range(len(sura_name)):
        main_markup.insert(f"{i + 1}.{sura_name[i]}")

    main_markup.row(back_button, main_menu_button)

    await message.answer("Oʻzingizga kerakli suraning raqamini kiriting, nomini yozing yoki tugmalardan foydalaning", reply_markup=main_markup)
    await my_State.Oyatlar.set()