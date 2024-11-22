from telebot import TeleBot, types
from button import Button
from callback import handle_callback

API_TOKEN = "7638229482:AAHBrrkTzgtOhKA2578MmfbBvHBbKwMbloM"  # Apna Telegram Bot Token yahan daalein
bot = TeleBot(API_TOKEN)

# Start Command
@bot.message_handler(commands=["start"])
def start(message):
    welcome_text = "स्वागत है! कृपया नीचे दिए गए 'Order Now' बटन पर क्लिक करें।"
    buttons = Button.order_now_button()
    bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup=buttons)

# Handle Callback
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    handle_callback(bot, call)

# Bot Run Karein
if __name__ == "__main__":
    bot.polling()
