from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "my first project",
    api_id = 
        15119900,
    api_hash = "35111ae010152c157cc56d8f107f800b",
    bot_token = "5616290541:AAG8J6aK1mBOh90sbA-sB5-8dZyTy5AyZlI"
)
START_MESSAGE_BUTTONS = [[InlineKeyboardButton(text='⚙️ Website', url='https://estar.games/')], 
[InlineKeyboardButton(text='🐦 Twitter', url='https://twitter.com/estartoken'), 
InlineKeyboardButton(text='💬 Discord', url='https://discord.gg/estar')], 
[InlineKeyboardButton(text='🌍 Telegram International Group', url='https://t.me/estartoken')], 
[InlineKeyboardButton(text='⬜️ Whitepaper', url='https://estar.gitbook.io/whitepaper-estar/about-estargames/project-introduction'), 
InlineKeyboardButton(text='🐎 Mint', url='https://www.frameit.gg/marketplace/EQUISTAR-3f393f/items')], 
[InlineKeyboardButton(text='🎟 Raffle', url='https://raffle.equistar.io/unlock'), 
InlineKeyboardButton(text='🏇 Equistar Game | dApp', url='https://equistar.estar.games/')]]

START_MESSAGE = "Hi! Follow these resources to learn more about EstarGames"
@bot.on_message(filters.command('info') & filters.group)
def command1(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        text = text,
        reply_markup=reply_markup,
        disable_web_page_preview = True
    )

#welcome
GROUP_RO = "https://t.me/estarromania"
WELCOME_MESSAGE_RO = "Salut si bine ai venit in comunitatea EstarGames! Scrie /info pentru mai multe informatii despre proiect."

GROUP = "https://t.me/estartoken"
WELCOME_MESSAGE = "Hello and welcome to the EstarGames community! Write /info for more information about the project."

@bot.on_message(filters.chat(GROUP_RO) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE_RO)

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)
    
    print("I am Alive")

bot.run()