from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "my first project",
    api_id = 
        15119900,
    api_hash = "35111ae010152c157cc56d8f107f800b",
    bot_token = "5616290541:AAG8J6aK1mBOh90sbA-sB5-8dZyTy5AyZlI"
)

token = [[InlineKeyboardButton(text='🌿 $ESTAR on JungleDEX', url='https://jungledex.com/analytics/tokens/ESTAR-461bab')], 
[InlineKeyboardButton(text='📊 Tokenomics', url='https://estar.gitbook.io/whitepaper-estar/tokenomics'), 
InlineKeyboardButton(text='🔀 Swap $ESTAR Token', url='https://swap.estar.games')]]

START_MESSAGE_BUTTONS = [[InlineKeyboardButton(text='⚙️ Website', url='https://estar.games/')], 
[InlineKeyboardButton(text='⬜️ Whitepaper', url='https://estar.gitbook.io/whitepaper-estar/about-estargames/project-introduction'), 
InlineKeyboardButton(text='🌿 $ESTAR on JungleDEX', url='https://sale.estar.games')], 
[InlineKeyboardButton(text='🐎 Equistar MINT', url='https://www.frameit.gg/marketplace/EQUISTAR-3f393f/items'), 
InlineKeyboardButton(text='🐎 EquiDAO MINT', url='https://www.frameit.gg/marketplace/EQUIDAO-0503e5/items')], 
[InlineKeyboardButton(text='🏇 Equistar Game | dApp', url='https://equistar.estar.games/')], 
[InlineKeyboardButton(text='🐦 Twitter', url='https://twitter.com/estartoken'), 
InlineKeyboardButton(text='💬 Discord', url='https://discord.estar.games')], 
[InlineKeyboardButton(text='🇷🇴 Telegram Group', url='https://t.me/estarromania'), 
InlineKeyboardButton(text='🌍 Telegram Group', url='https://t.me/estartoken')],
[InlineKeyboardButton(text='📢 Estar Announcements Channel', url='https://t.me/estarannouncements')],]

TOKEN_MESSAGE = "For any information related to the **$ESTAR** token, see the links below!"

START_MESSAGE = "👋 Hi! Follow these resources to learn more about **EstarGames** 🔥"
@bot.on_message(filters.command('info') & filters.group)
def command1(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        text = text,
        reply_markup=reply_markup,
        disable_web_page_preview = True
    )

@bot.on_message(filters.command('token') & filters.group)
def command1(bot, message):
    text = TOKEN_MESSAGE
    reply_markup = InlineKeyboardMarkup(token)
    message.reply(
        text = text,
        reply_markup=reply_markup,
        disable_web_page_preview = True
    )


RULES = " 📌  **#EstarGames** Community Rules:\n➛ Without offending anyone, any problem you have can be solved; \n➛ No promotions, only if you talked to one of the admins **(@sitaruestar, @qkcostii)**;\n➛ No spam;\n➛ No bad jokes or jokes about other people / projects;\n➛ Any partnership can be discussed privately **(@sitaruestar, @qkcostii)**.\n\n❗️If you missed a day, we recommend you look in **pinned-message** to be up to date with all the announcements from that day, and not only that."

@bot.on_message(filters.command('rules') & filters.group)
def command1(bot, message):
    text = RULES
    message.reply(
        text = text
        
    )

#welcome
GROUP_RO = 'estarromania'
WELCOME_MESSAGE_RO = "👋 Salut si bine ai venit in comunitatea **EstarGames**!\n\nScrie **/info** pentru mai multe informatii despre proiect si **/rules** pentru regulile comunitatii."

GROUP = 'estartoken'
WELCOME_MESSAGE = "👋 Hello and welcome to the **EstarGames** community!\n\nWrite **/info** for more informations about the project and **/rules** for the community's rules."

@bot.on_message(filters.chat(GROUP_RO) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE_RO)

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)

    print("I am Alive")
bot.run()