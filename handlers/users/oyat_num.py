from loader import db, dp
from aiogram import types
from states.full import my_State
from keyboards.default.start import main_markup
from aiogram.dispatcher import FSMContext
import requests


@dp.message_handler(state=my_State.Oyatlar_num)
async def send_oyats(message: types.Message, state: FSMContext):
    data = await state.get_data()
    the_name = data.get("the_name")
    chapter = data.get("the_chapter")
    the_num_verse = data.get("the_num_verse")
    the_number = message.text
    if the_number.isdigit():
        r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json").json()
        for sura in r['quran']:
            if int(sura['chapter']) == int(chapter) and int(sura['verse']) == int(the_number):
                await message.answer(f"{the_name} surasi {the_number}-surasi \n\n"
                                     f"{sura['text']}")
            else:
                pass
    elif the_number.__contains__("-"):
        back = the_number.split('-')[:1]
        back = back[0]#[2:len(message.text)]
        front = the_number.split('-')[1::]
        front = front[0]
        if front.isdigit() and back.isdigit():
            if int(front) > the_num_verse:
                await message.answer(f"bu surada {the_num_verse} ta sura bor\n"
                                     f"siz {back}-{front} deb yozdingiz\n"
                                     f"qaytadan kiriting")
            else:
                for i in range(int(back), int(front) + 1):
                    print(i)
                    r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json").json()
                    for sura in r['quran']:
                        if int(sura['chapter']) == int(chapter) and int(sura['verse']) == int(i):
                            await message.answer(f"{the_name} surasi {i}-surasi \n\n"
                                                 f"{sura['text']}")
                        else:
                            pass
        else:
            await message.answer("raqamlarni to'gri kiriting")

    else:
        await message.answer("son kiriting")