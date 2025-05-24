# main.py
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from memory import get_user_data, update_user_data

SCENARIOS = {
    "romantis": "dengan nada lembut dan penuh cinta",
    "petualangan": "dengan semangat petualang dan keberanian",
    "teman": "santai dan bersahabat",
    "sahabat": "dalam dan penuh perhatian",
    "musuh jadi kekasih": "dengan ketegangan dan perasaan tersembunyi",
    "teman jadi pacar": "dengan perasaan malu-malu tapi berkembang",
    "cinta pertama": "dengan emosi manis dan nostalgia",
    "cinta terlarang": "dengan suasana rahasia dan konflik"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    update_user_data(user.id, "scenario", "teman")
    await update.message.reply_text(
        f"Hai {user.first_name}, aku Hinata AI 💜\n"
        f"Ayo ngobrol! Kamu bisa pilih skenario dengan /tema nama_skenario\n"
        f"Cth: /tema romantis"
    )

async def tema(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not context.args:
        await update.message.reply_text("Ketik /tema [nama_skenario], contoh: /tema sahabat")
        return

    tema = " ".join(context.args).lower()
    if tema in SCENARIOS:
        update_user_data(user.id, "scenario", tema)
        await update.message.reply_text(f"Skenario diubah ke: {tema.upper()}. Yuk lanjutkan obrolan 💬")
    else:
        await update.message.reply_text("Tema tidak dikenali. Coba: romantis, petualangan, teman, sahabat, dll.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    user_data = get_user_data(user.id)
    skenario = user_data.get("scenario", "teman")
    style = SCENARIOS.get(skenario, "")

    # Simulasikan respons dari Hinata
    response = (
        f"(Hinata - {skenario})\n"
        f"Aku mengerti... {text}\n"
        f"Aku akan menanggapi {style} 💬"
    )

    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tema", tema))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot berjalan...")
    app.run_polling()

if __name__ == '__main__':
    main()
