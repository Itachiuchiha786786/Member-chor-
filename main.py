from telebot import TeleBot
from button import Button
from callback import handle_callback

API_TOKEN = "7638229482:AAHBrrkTzgtOhKA2578MmfbBvHBbKwMbloM"  # Apna Telegram Bot Token yahan daalein
bot = TeleBot(API_TOKEN)

# User data tracking for temporary states
user_data = {}

# Start Command
@bot.message_handler(commands=["start"])
def start(message):
    welcome_text = "स्वागत है! कृपया नीचे दिए गए 'Order Now' बटन पर क्लिक करें।"
    buttons = Button.order_now_button()
    bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup=buttons)

# Handle Callback Queries
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global user_data

    if call.data == "order_now":
        bot.send_message(call.message.chat.id, "कृपया अपना पब्लिक लिंक भेजें।")
        user_data[call.message.chat.id] = {"step": "awaiting_link"}  # Track user state

    handle_callback(bot, call)

# Handle Public Link from User
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "awaiting_link")
def handle_public_link(message):
    global user_data
    public_link = message.text

    # Validate if public link is a URL
    if "http://" in public_link or "https://" in public_link:
        user_data[message.chat.id]["public_link"] = public_link
        user_data[message.chat.id]["step"] = "price_selection"

        bot.send_message(
            message.chat.id, 
            "धन्यवाद! नीचे दिए गए बटन से अपना सदस्यता पैकेज चुनें।", 
            reply_markup=Button.price_list_buttons()
        )
    else:
        bot.send_message(message.chat.id, "कृपया एक सही पब्लिक लिंक भेजें।")

# Bot Execution
if __name__ == "__main__":
    bot.polling()
