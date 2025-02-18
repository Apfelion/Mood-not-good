from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random

# Replace '8107962560:AAFH71DYefKsK6_bwnd-drxSLzQ7WDSh1OM' with your actual bot token
TOKEN = "8107962560:AAFH71DYefKsK6_bwnd-drxSLzQ7WDSh1OM"

async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is used."""
    await update.message.reply_text("Hello! I'm your Mood Booster Bot 😊. Type /boostme to get a motivation boost!")

async def boostme(update: Update, context: CallbackContext) -> None:
    """Send a motivational message when the /boostme command is used."""
    messages = [
        "Keep calm and let go of that shit!", 
        "You`re a badass, don`t forget that!🌟", 
        "Laugh it off, life`s too short!",  
        "Some people just need a high-five. In the face. With a chair.", 
        "U could slapped that moron but that would be animal abuse.", 
        "Coffee, deep breath, and move on.🚀",  
        "No stress, just vibes!☀️", 
        "If you can`t convince them, confuse them", 
        "An apple a day keeps anyone away if you throw it hard enough.💪", 
        "It happened again. Someone left the bag with idiots open."
    ]
    await update.message.reply_text(random.choice(messages))

def main():
    """Start the bot."""
    app = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("boostme", boostme))

    # Run the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()