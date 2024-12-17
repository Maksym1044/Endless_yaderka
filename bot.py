from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вітаю в постапокаліптичному світі!\nГотуйся до виживання у своєму бункері.\n"
        "Використовуй /help для перегляду команд."
    )

# команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Список доступних команд:\n"
        "/start - Почати гру\n"
        "/help - Допомога\n"
        "/create_bunker - Створити бункер\n"
        "/profile - Переглянути профіль\n"
        "/explore - Відправитись на експедицію\n"
        "/pvp - Викликати на дуель"
    )

# головна функція
def main():
    TOKEN = '7389962422:AAEqz6wDaHLOe2SvkPm1jSWE-2fJuTb-Ur4'
    app = ApplicationBuilder().token(TOKEN).build()

    # обробники команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()



