import requests
from aiogram.types import ReplyKeyboardMarkup

from loader import db, dp
from aiogram import types
from states.full import my_State
from keyboards.default.start import main_markup, back_button, main_menu_button
from aiogram.dispatcher import FSMContext
# from keyboards.default.start import get_category_markup, get_product_markup


@dp.message_handler(text="🏠 Asosiy menyuga qaytish", state="*")
async def main_menu_redirect(message: types.Message, state:FSMContext):
    await message.answer("Kerakli surani tanlang", reply_markup=main_markup)
    await my_State.Suralar.set()


@dp.message_handler(text = "🔙 Orqaga", state=my_State.Oyatlar)
async def redirect(message: types.Message, state:FSMContext):
    await message.answer("Kerakli surani tanlang", reply_markup=main_markup)
    await my_State.Suralar.set()

@dp.message_handler(text = "🔙 Orqaga", state=my_State.Oyatlar_num)
async def redirect(message: types.Message, state:FSMContext):
    r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json").json()
    main_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    sura_name = []
    for sura in r['chapters']:
        sura_name.append(sura['name'])

    for i in range(len(sura_name)):
        main_markup.insert(f"{i + 1}.{sura_name[i]}")

    main_markup.row(back_button, main_menu_button)

    await message.answer("Oʻzingizga kerakli suraning raqamini kiriting, nomini yozing yoki tugmalardan foydalaning",
                         reply_markup=main_markup)
    await my_State.Oyatlar.set()
#
# @dp.message_handler(text = "🔙 Orqaga", state=ShopState.amount)
# async def product_redirect(message: types.Message, state:FSMContext):
#     data = await state.get_data()
#     cat_id = data.get("cat_id")
#     products = await db.select_products_by_category(cat_id=cat_id)
#     if products:
#         markup = await get_product_markup(products=products)
#         await message.answer(f"Ushbu bo'limdan kerakli mahsulotni tanlang", reply_markup=markup)
#         await ShopState.product.set()