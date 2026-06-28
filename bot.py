import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8934584601:AAGiog85GcNA8FU0lILEKCyp_0fXgiM8n80"
CHANNEL = "@zulpanov_tarix"
URL = "https://testtarixzulpanov.vercel.app"

async def check(uid, ctx):
    try:
        m = await ctx.bot.get_chat_member(CHANNEL, uid)
        return m.status in ["member","administrator","creator"]
    except:
        return False

async def start(u: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if await check(u.effective_user.id, ctx):
        await u.message.reply_text("✅ Testni boshlang!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Test", web_app=WebAppInfo(url=URL))]]))
    else:
        await u.message.reply_text("Kanalga a'zo bo'ling!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📢 Kanal", url="https://t.me/zulpanov_tarix")],[InlineKeyboardButton("✅ Tekshirish", callback_data="c")]]))

async def btn(u: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = u.callback_query
    await q.answer()
    if await check(q.from_user.id, ctx):
        await q.edit_message_text("✅ Testni boshlang!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Test", web_app=WebAppInfo(url=URL))]]))
    else:
        await q.answer("A'zo emassiz!", show_alert=True)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(btn))
    app.run_polling()

