from loader import db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_markup.add(KeyboardButton(text="Umumiy izlash🔎"), "Oyatlar")
main_markup.row("Suradan izlash", "Sozlamalar")
main_markup.add("Fikr bildirish✍️")

back_button = (KeyboardButton(text="🔙 Orqaga"))
main_menu_button = (KeyboardButton(text="🏠 Asosiy menyuga qaytish"))


# async  def get_category_markup():
#     categories = await db.select_all_cats()
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for category in categories:
#         markup.insert(KeyboardButton(text=category["title"]))
#     markup.add(cart_button,  buy_button, back_button, main_menu_button)
#     return markup
#
# async def get_product_markup(products):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     for product in products:
#         markup.insert(KeyboardButton(text=product['title']))
#     markup.add(cart_button, buy_button, back_button, main_menu_button, )
#     return markup
#
# async def numbers_markup(number=9):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     for i in range(1, number+1):
#         markup.insert(KeyboardButton(text=str(i)))
#     markup.add(cart_button, back_button)
#     return markup
#
# async def cart_items_markup(products):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     for product in products:
#         markup.insert(KeyboardButton(text=f"❌ {product} ❌"))
#     markup.row(buy_button, clear_button)
#     markup.row(back_button, main_menu_button)
#     return markup