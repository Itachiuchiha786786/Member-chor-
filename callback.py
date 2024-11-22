from button import Button

def handle_callback(bot, call):
    if call.data == "order_now":
        bot.send_message(call.message.chat.id, "कृपया अपना पब्लिक लिंक भेजें।")
    elif call.data.startswith("price_"):
        if call.data == "price_10":
            price = "₹50"
        elif call.data == "price_50":
            price = "₹200"
        elif call.data == "price_100":
            price = "₹400"
        else:
            price = "Unknown"

        bot.send_message(
            call.message.chat.id, 
            f"आपने {price} के लिए चुना है। कृपया नीचे दिए गए 'Pay Now' बटन पर क्लिक करें।",
            reply_markup=Button.pay_now_button()
        )
    elif call.data == "payment_done":
        bot.send_message(call.message.chat.id, "धन्यवाद! कृपया 10 मिनट प्रतीक्षा करें।")

        # Channel पर डिटेल भेजें
        channel_id = "@FREE_PROMO_OFF"
        bot.send_message(channel_id, f"Order Details:\nUser: {call.from_user.id}\nAmount: {price}")
