from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,WebAppInfo
from telegram.ext import Application,CommandHandler,ContextTypes
TOKEN="8934584601:AAGiog85GcNA8FU0lILEKCyp_0fXgiM8n80"
URL="https://testtarixzulpanov.vercel.app"
async def start(u,c):
 await u.message.reply_text("📚 ZULPANOV TARIX TEST\n\nTestni boshlang 👇",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Testni boshlash",web_app=WebAppInfo(url=URL))]]))
app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.run_polling()
