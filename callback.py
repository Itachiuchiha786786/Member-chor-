from button import Button

def handle_callback(bot, call, user_data):
    if call.data.startswith("price_"):
        if call.data == "price_200":
            price = "₹100"
            members = "200 Mᴇᴍʙᴇʀs"
        elif call.data == "price_500":
            price = "₹250"
            members = "500 Mᴇᴍʙᴇʀs"
        elif call.data == "price_1000":
            price = "₹450"
            members = "1000 Mᴇᴍʙᴇʀs"
        elif call.data == "price_2000":
            price = "₹800"
            members = "2000 Mᴇᴍʙᴇʀs"
        elif call.data == "price_5000":
            price = "₹1500"
            members = "5000 Mᴇᴍʙᴇʀs"
        else:
            price = "Unknown"
            members = "Unknown"

        if call.message.chat.id not in user_data:
            user_data[call.message.chat.id] = {}
        user_data[call.message.chat.id]["price"] = price
        user_data[call.message.chat.id]["members"] = members

        bot.send_message(
            call.message.chat.id,
            f"आपने {members} के लिए {price} चुना है। कृपया नीचे दिए गए 'Pay Now' बटन पर क्लिक करें।",
            reply_markup=Button.pay_now_button(),
        )

    elif call.data == "payment_done":
        bot.send_message(
            call.message.chat.id,
            "धन्यवाद! हमने आपका भुगतान प्राप्त कर लिया है। कृपया 10 मिनट प्रतीक्षा करें।",
        )

        channel_id = "@FREE_PROMO_OFF"  # Replace with your admin channel username
        order_details = user_data.get(call.message.chat.id, {})
        public_link = order_details.get("public_link", "N/A")
        price = order_details.get("price", "N/A")
        members = order_details.get("members", "N/A")

        msg = bot.send_message(
            channel_id,
            f"📦 **New Order**\n\n"
            f"👤 **User ID**: {call.from_user.id}\n"
            f"📎 **Public Link**: {public_link}\n"
            f"👥 **Members**: {members}\n"
            f"💰 **Amount**: {price}\n"
            f"📌 **Status**: Pending",
        )

        user_data[call.message.chat.id]["channel_message_id"] = msg.message_id
