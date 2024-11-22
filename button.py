from telebot import types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo

# Assuming you're using Pyrogram for callback handling
app = Client("my_bot")

class Button:
    @staticmethod
    def order_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Oʀᴅᴇʀ ɴᴏᴡ", callback_data="order_now"))
        markup.add(types.InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+OL6jdTL7JAJjYzVl"))
        return markup

    @staticmethod
    def price_list_buttons():
        markup = types.InlineKeyboardMarkup()

        # First row: Price buttons
        markup.row(
            types.InlineKeyboardButton("➊", callback_data="price_200"),
            types.InlineKeyboardButton("➋", callback_data="price_500"),
            types.InlineKeyboardButton("➌", callback_data="price_1000"),
            types.InlineKeyboardButton("➍", callback_data="price_2000"),
            types.InlineKeyboardButton("➎", callback_data="price_5000")
        )

        # Second row: Owner button
        markup.add(
            types.InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+OL6jdTL7JAJjYzVl")
        )

        # Third row: Support and Update buttons
        markup.row(
            types.InlineKeyboardButton("Oᴡɴᴇʀ", url="https://t.me/UTTAM470"),
            types.InlineKeyboardButton("Co Oᴡɴᴇʀ", url="https://t.me/llMR_VAMPIRE_KINGll")
        )

        return markup

    @staticmethod
    def pay_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                "Pᴀʏ ɴᴏᴡ", 
                callback_data="payment"  # Redirect to a general payment link
            )
        )
        markup.add(
            types.InlineKeyboardButton(
                "Pᴀʏᴍᴇɴᴛ ᴅᴏɴᴇ 👍", callback_data="payment_done"
            )
        )
        return markup

# Corrected callback handler with filters
@app.on_callback_query(filters.regex("payment"))
async def gib_repo(client, callback_query):
    await callback_query.edit_message_media(
        InputMediaVideo("https://files.catbox.moe/vfn74b.jpg"),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingsback_helper")]]
        ),
    )
