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
        markup.add(types.InlineKeyboardButton("10 Members - ₹50", callback_data="price_10"))
        markup.add(types.InlineKeyboardButton("50 Members - ₹200", callback_data="price_50"))
        markup.add(types.InlineKeyboardButton("100 Members - ₹400", callback_data="price_100"))
        return markup

    @staticmethod
    def pay_now_button():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Pay Now", url="upi://pay?pa=uk977061@axl&pn=YourName&am=Amount"))
        return markup