from telebot import types

class Button:
    @staticmethod
    def order_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Oʀᴅᴇʀ ɴᴏᴡ", callback_data="order_now"))
        markup.add(types.InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+OL6jdTL7JAJjYzVl"))
        return markup

    @staticmethod
    def price_list_buttons():
        # Creating inline keyboard
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
                "Pᴀʏ ɴᴏᴡ", callback_data="pay_now_image"  # Change callback_data to handle the image
            )
        )
        markup.add(
            types.InlineKeyboardButton(
                "Pᴀʏᴍᴇɴᴛ ᴅᴏɴᴇ 👍", callback_data="payment_done"
            )
        )
        return markup

# This method needs to handle the callback
def handle_callback(call):
    if call.data == "pay_now_image":
        # Send the image directly to the user
        bot.send_photo(call.message.chat.id, "https://files.catbox.moe/vfn74b.jpg")  # The image URL here
