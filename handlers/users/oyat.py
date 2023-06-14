from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db, dp
from aiogram import types
from states.full import my_State
from keyboards.default.start import main_markup, back_button, main_menu_button
from aiogram.dispatcher import FSMContext
import json
import requests


@dp.message_handler(state=my_State.Oyatlar)
async def send_oyats(message: types.Message, state: FSMContext):
    r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json").json()
    try:
        the_name = message.text.split('.')[1::]
        the_name = the_name[0]#[2:len(message.text)]
        the_chapter = message.text.split('.')[::1]
        the_chapter = the_chapter[0]
        await state.update_data(data={"the_name": the_name})
        await state.update_data(data={"the_chapter": the_chapter})
        the_num_verse = 0
        smth = True
        for sura in r['chapters']:
            if sura['name'] == the_name:
                the_num_verse += len(sura["verses"])

        # for i in range(len(sura_name)):
        #     main_markup.insert(f"{i + 1}.{sura_name[i]}")
        try:
            for sura in r['chapters']:
                if the_name in sura['name']:
                    smth = False
            if smth:
                raise NameError
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(back_button, main_menu_button)
            await message.answer(f"{the_name} surasi {the_num_verse} ta oyatdan iborat \n"
                                 "o'qimoqchi bo'lgan oyatingizning raqamini kiriting \n"
                                 "yoki ko'proq oyat o'qimoqchi bo'lsangiz oyatlarni quyidagi ko'rinishda kiriting\n"
                                 "➡️  2,5,12,13 ....\n"
                                 "Yoki \n"
                                 "➡️  1-5 ko'rinishida xabar jo'nating\n"
                                 f"Suraning barcha oyatlarni o'qish uchun 1-{the_num_verse} deb xabar jo'nating" ,reply_markup=markup)

            await state.update_data(data={"the_num_verse": the_num_verse})
            await my_State.Oyatlar_num.set()

        except NameError:
            await message.answer("qaytadan kiriting")
    except IndexError:
        await message.answer("unday sura topilmadi")



