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
            types.InlineKeyboardButton("👑 Owner", url="https://t.me/your_owner_username")
        )

        # Third row: Support and Update buttons
        markup.row(
            types.InlineKeyboardButton("🛠 Support", url="https://t.me/your_support_channel"),
            types.InlineKeyboardButton("🔔 Update", url="https://t.me/your_update_channel")
        )

        return markup

    @staticmethod
    def pay_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                "Pᴀʏ ɴᴏᴡ", 
                url="https://files.catbox.moe/vfn74b.jpg"  # Redirect to a general payment link
            )
        )
        markup.add(
            types.InlineKeyboardButton(
                "Pᴀʏᴍᴇɴᴛ ᴅᴏɴᴇ 👍", callback_data="payment_done"
            )
        )
        return markup
