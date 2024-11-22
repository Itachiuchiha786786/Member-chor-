from telebot import TeleBot
from button import Button
from callback import handle_callback

API_TOKEN = "7638229482:AAHBrrkTzgtOhKA2578MmfbBvHBbKwMbloM"  # Replace with your actual bot token
OWNER_ID = "7400383704"  # Replace with your Telegram user ID (as the bot owner)
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
    if call.data == "order_now":
        bot.send_message(call.message.chat.id, "कृपया अपना पब्लिक लिंक भेजें।")
        user_data[call.message.chat.id] = {"step": "awaiting_link"}
    handle_callback(bot, call, user_data)

# Handle Public Link from User
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "awaiting_link")
def handle_public_link(message):
    public_link = message.text
    if "http://" in public_link or "https://" in public_link:
        user_data[message.chat.id]["public_link"] = public_link
        user_data[message.chat.id]["step"] = "price_selection"

        bot.send_message(
            message.chat.id,
            "धन्यवाद! नीचे दिए गए बटन से अपना सदस्यता पैकेज चुनें।",
            reply_markup=Button.price_list_buttons(),
        )
    else:
        bot.send_message(message.chat.id, "कृपया एक सही पब्लिक लिंक भेजें।")

# Command to Mark Orders as Complete
@bot.message_handler(commands=["done"])
def mark_order_done(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "आपके पास इस आदेश को पूरा करने की अनुमति नहीं है।")
        return

    try:
        _, user_id = message.text.split()
        user_id = int(user_id)
    except ValueError:
        bot.reply_to(message, "कृपया सही फॉर्मेट में कमांड दर्ज करें: /done <user_id>")
        return

    if user_id not in user_data or "channel_message_id" not in user_data[user_id]:
        bot.reply_to(message, "कोई लंबित आदेश नहीं मिला।")
        return

    channel_id = "@FREE_PROMO_OFF"  # Replace with your admin channel username
    message_id = user_data[user_id]["channel_message_id"]

    try:
        bot.edit_message_text(
            chat_id=channel_id,
            message_id=message_id,
            text=f"📦 **New Order**\n\n"
                 f"👤 **User ID**: {user_id}\n"
                 f"📎 **Public Link**: {user_data[user_id].get('public_link', 'N/A')}\n"
                 f"👥 **Members**: {user_data[user_id].get('members', 'N/A')}\n"
                 f"💰 **Amount**: {user_data[user_id].get('price', 'N/A')}\n"
                 f"📌 **Status**: Complete"
        )
        bot.reply_to(message, "आदेश को 'Complete' चिह्नित कर दिया गया है।")
    except Exception as e:
        bot.reply_to(message, f"त्रुटि: {e}")

# Bot Execution
if __name__ == "__main__":
    bot.polling()
