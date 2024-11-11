import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """
    Sending welcome message to the user
    """
    bot.reply_to(
        message,
        "Hi! Welcome to the NYU Meal Plan Bot. Please type /help to see the available commands.",
    )


@bot.message_handler(commands=["help"])
def send_help(message):
    """
    Sending welcome message to the user
    """
    bot.reply_to(
        message,
        "Here are the available commands:\n",
        reply_markup=telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True, row_width=2
        ).add(
            telebot.types.KeyboardButton("/get_plan"),
            telebot.types.KeyboardButton("/get_balances"),
        ),
    )


bot.infinity_polling()
