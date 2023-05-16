import qrcode
import telebot

# Create a Telegram bot.
bot = telebot.TeleBot("6240560190:AAEMwdg8GCGgb3xF_T8Fa4m8OcLsvJptKIc")


# Define a function that will handle the /start command.
@bot.message_handler(commands=["start"])
def start(message):
    # Send a message to the user asking for their link.
    bot.send_message(message.chat.id, "Enter your link: ")


# Define a function that will handle the incoming links.
@bot.message_handler(content_types=["text"])
def link(message):
    # Create a QR code object.
    qr = qrcode.make(message.text)

    # Save the QR code to a file.
    qr.save("qr_code.png")

    # Send the QR code image to the user.
    bot.send_photo(message.chat.id, open("qr_code.png", "rb"))


# Start the bot.
bot.polling()
