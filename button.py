from telebot import types

class Button:
    @staticmethod
    def order_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Order Now", callback_data="order_now"))
        return markup

    @staticmethod
    def price_list_buttons():
        markup = types.InlineKeyboardMarkup()  # Properly indented
        # Add all buttons in one row
        markup.row(
            types.InlineKeyboardButton("𝙰", callback_data="price_200"),
            types.InlineKeyboardButton("𝙱", callback_data="price_500"),
            types.InlineKeyboardButton("𝙲", callback_data="price_1000"),
            types.InlineKeyboardButton("𝙳", callback_data="price_2000"),
            types.InlineKeyboardButton("𝙴", callback_data="price_5000")
        )
        return markup

    @staticmethod
    def pay_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                "Pay Now", 
                url="https://www.phonepe.com/"  # Redirect to a general payment link
            )
        )
        markup.add(
            types.InlineKeyboardButton(
                "मैंने भुगतान किया", callback_data="payment_done"
            )
        )
        return markup
