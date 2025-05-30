from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = '7604244774:AAHCkQ9r_6OVYIBv7dTaCKHHXp8ZaqJInyk'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ADMIN 👑", callback_data='admin')],
        [InlineKeyboardButton("BASIC GUIDELINE M3TH ✋", callback_data='guideline')],
        [InlineKeyboardButton("AN!ME IMP 🥴", callback_data='anime')],
        [InlineKeyboardButton("AGED ACC 👽", callback_data='aged')],
        [InlineKeyboardButton("LONG BIO METHOD 🤡", callback_data='bio')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌟 **Main Menu** 🌟", reply_markup=reply_markup, parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'admin':
        text = "👑 **Admin Instructions** 👑\n\n1️⃣ Step one...\n2️⃣ Step two...\n\n⬅️ /start to return."
    elif data == 'guideline':
        text = "✋ **Basic Guideline M3TH**\n\n15. Go and type your email into the reset box.\n16. Press send link...\n\n⬅️ /start to return."
    elif data == 'anime':
        text = "🥴 **Anime IMP Details**\n\nDescription or steps...\n\n⬅️ /start to return."
    elif data == 'aged':
        text = "👽 **Aged Account Instructions**\n\nDescription or steps...\n\n⬅️ /start to return."
    elif data == 'bio':
        text = "🤡 **Long Bio Method**\n\nDescription or steps...\n\n⬅️ /start to return."
    else:
        text = "Unknown option."

    await query.edit_message_text(text=text, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is running...")
    app.run_polling()