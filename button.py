from telebot import types

class Button:
    @staticmethod
    def order_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Order Now", callback_data="order_now"))
        return markup

    @staticmethod
    def price_list_buttons():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("1", callback_data="1"))
        markup.add(types.InlineKeyboardButton("2", callback_data="2"))
        markup.add(types.InlineKeyboardButton("3", callback_data="3"))
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
