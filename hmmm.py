## fban.message
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("BOT TOKEN", skip_pending=True)

@bot.message_handler(commands=["start"])
def menu(message):
    markup = InlineKeyboardMarkup(row_width=2)
    kanal = InlineKeyboardButton("📣 Kanalımız", url="KANAL")
    markup.add(kanal)
    bot.send_message(message.chat.id, """
*Spam Protector*

_Gruplarınızı Korumak Amacı İle Yapılan Bir Bottur Botun Mantığı Spam Barındıran İçerikleri Gizlediği İçin Grubunuz Spama Düşmez Bölelikle Spam Tehlikesi Ortadan Kalkar_

*Yapmanız Gerekenler*

•Grubunuza Eklemek.
•Full Yetkiye Sahip Olması İle Grubunuz Güvende Olacaktır.
""", reply_markup=markup, parse_mode="Markdown")

prnt("Bot Aktif")
Öç
iif name =="__main__":
    bot.polling(none_stop=True)

user/id:1242148130

.botpick/fbanal:=
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from userbot.events import register
from userbot import bot
from asyncio import sleep


@register(outgoing=True, pattern="^.fbanall ?(\w*)")
async def deneme(event: NewMessage.Event):
    reason = ""
    text: str = event.message.text.split()
    try:
        reason = " ".join(text[2:])
    except:
        pass
    _id: str = text[1]
    if _id.startswith("@"):
        _id = _id.replace("@", "")
    async for user in event.client.iter_participants(_id):
        if not user.bot:
            await bot.send_message(event.chat_id, f"/fban {user.id} {reason}")
            await sleep(0.5)


Komut = CmdHelp('hmm')
Komut.add_info('Sebep yazmak zorunlu değildir.')
Komut.add()
