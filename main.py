from telebot import TeleBot
from button import Button
from callback import handle_callback

API_TOKEN = "7850537170:AAH5ANR4RVQ3EPXET_aiF5AOAOAes7XR5jE"  # Replace with your actual bot token
OWNER_ID = 7400383704  # Replace with your Telegram user ID (as the bot owner)
BABY_CHANNEL_USERNAME = "@BABY09_WORLD"  # Replace with your music channel username
bot = TeleBot(API_TOKEN)

# User data tracking for temporary states
user_data = {}

# Check if user is a member of the music channel
def is_user_member_of_baby_channel(user_id):
    try:
        member = bot.get_chat_member(BABY_CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

# Start Command with Music Join Check
@bot.message_handler(commands=["start"])
def start(message):
    # Check if the user is a member of the music channel
    if not is_user_member_of_baby_channel(message.chat.id):
        bot.send_message(
            message.chat.id, 
            f"Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ channel ғɪʀsᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ: {BABY_CHANNEL_USERNAME}."
        )
        return

    welcome_text = (
    "╭────────〔༻༺〕────────╮\n‎ ‎  ‌‎   ‌‎Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍᴇᴍʙᴇʀ Bᴏᴏsᴛɪɴɢ !\n   ━━━━━━━━━༻❁༺━━━━━━━━━\n"
    "‌‌‌‌    Aɴʏ ᴘʀᴏʙʟᴇᴍ ᴠɪsɪᴛ ʜᴇʀᴇ :- Sᴜᴘᴘᴏʀᴛ\n‌‌             Pᴀɪᴅ ʙᴏᴏsᴛɪɴɢ ᴀᴠᴀɪʟᴀʙʟᴇ \n‌‌‌‎                      𝙾 𝚁 𝙳 𝙴 𝚁  𝙽 𝙾 𝚆!!\n╰────────〔༻༺〕────────╯"
    )
    buttons = Button.order_now_button()
    bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup=buttons)

# Handle Callback Queries
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "order_now":
        bot.send_message(call.message.chat.id, "Nᴏᴡ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ [ᴘᴜʙʟɪᴄ]")
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
            """⌨ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗥𝗘𝗔𝗟 𝗠𝗘𝗠𝗕𝗘𝗥 ⌨
┏━━━━━━━༻❁༺━━━━━━━┓
「➊」:- ₹100 ⇝200 Mᴇᴍʙᴇʀ

「➋」:- ₹250 ⇝500 Mᴇᴍʙᴇʀ

「➌」:- ₹450 ⇝1000 Mᴇᴍʙᴇʀ

「➍」:- ₹800 ⇝2000 Mᴇᴍʙᴇʀ

「➎」:- ₹1500 ⇝5000 Mᴇᴍʙᴇʀ
┗━━━━━━━༻❁༺━━━━━━━┛
「Nᴏᴛᴇ」¹:- Oᴛʜᴇʀ sᴇʀᴠɪᴄᴇ ᴀᴠᴀɪʟᴀʙʟᴇ
ᴄᴏɴᴛᴀᴄᴛ : ‌‌➛ Oᴡɴᴇʀ / Cᴏ ᴏᴡɴᴇʀ

「Nᴏᴛᴇ」²:- Aɴʏ ᴘᴀʏᴍᴇɴᴛ ɪssᴜᴇ ᴄᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ / Cᴏ ᴏᴡɴᴇʀ
ᴀɴᴅ Cᴏᴍᴇ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ""",
            reply_markup=Button.price_list_buttons(),
        )
    else:
        bot.send_message(message.chat.id, "Yᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴇɴᴅ ᴀ [ᴘᴜʙʟɪᴄ/ᴠᴀʟɪᴅ] ʟɪɴᴋ ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")

@bot.message_handler(commands=["done"])
def mark_order_done(message):
    if message.from_user.id != OWNER_ID:
        # If the command is not from the owner, do nothing
        return

    try:
        _, user_id = message.text.split()
        user_id = int(user_id)  # Convert user_id to integer
    except ValueError:
        bot.reply_to(message, "Wʀᴏɴɢ ᴜsᴇs 🤪: /done <user_id>")
        return

    # Ensure the user_id exists in user_data and has a saved message_id
    if user_id not in user_data or "channel_message_id" not in user_data[user_id]:
        bot.reply_to(message, "Nᴏ sᴍs ғᴏᴜɴᴅ।")
        return

    # Get the channel message_id and edit it
    channel_id = "@FREE_PROMO_OFF"  # Replace with your admin channel username
    message_id = user_data[user_id]["channel_message_id"]

    try:
        # Edit the status in the message
        bot.edit_message_text(
            chat_id=channel_id,
            message_id=message_id,
            text=f"📦 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 𝗢𝗥𝗗𝗘𝗥 ✔️\n\n"
                 f"👤 Usᴇʀ ɪᴅ: {user_id}\n"
                 f"📎 Oʀᴅᴇʀ ʟɪɴᴋ: {user_data[user_id].get('public_link', 'N/A')}\n"
                 f"👥 Mᴇᴍʙᴇʀ: {user_data[user_id].get('members', 'N/A')}\n"
                 f"💰 Aᴍᴏᴜɴᴛ: {user_data[user_id].get('price', 'N/A')}\n"
                 f"📌 Sᴛᴀᴛᴜs: Cᴏᴍᴘʟᴇᴛᴇ 🥰"
        )
        bot.reply_to(message, "Oʀᴅᴇʀ ᴄᴏᴍᴘʟᴇᴛᴇ 💕")
    except Exception as e:
        bot.reply_to(message, f"त्रुटि: {e}")


# Bot Execution
if __name__ == "__main__":
    bot.polling()
