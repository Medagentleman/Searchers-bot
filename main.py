import telebot
from telebot import types
import logging

# Вставь сюда свой токен
TOKEN = 'XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX'

bot = telebot.TeleBot(TOKEN)

# Настройка логирования
logger = logging.getLogger('bot_logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('bot_activity.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_user_action(user, action):
    user_info = (f"User ID: {user.id}, Name: {user.first_name}, "
                 f"Last Name: {user.last_name}, Username: @{user.username}, Action: {action}")
    logger.info(user_info)

def send_search_keyboard(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=4)

    buttons = [
        types.InlineKeyboardButton('🔍 Google', callback_data='https://www.google.com'),
        types.InlineKeyboardButton('🌐 Yandex', callback_data='https://www.yandex.com'),
        types.InlineKeyboardButton('🔎 Bing', callback_data='https://www.bing.com'),
        types.InlineKeyboardButton('🟣 Yahoo', callback_data='https://www.yahoo.com'),
        types.InlineKeyboardButton('🦆 DuckDuckGo', callback_data='https://www.duckduckgo.com'),
        types.InlineKeyboardButton('🐉 Baidu', callback_data='https://www.baidu.com'),
        types.InlineKeyboardButton('🧠 WolframAlpha', callback_data='https://www.wolframalpha.com'),
        types.InlineKeyboardButton('🌱 Ecosia', callback_data='https://www.ecosia.org'),
        types.InlineKeyboardButton('🔐 StartPage', callback_data='https://www.startpage.com'),
        types.InlineKeyboardButton('🔍 Qwant', callback_data='https://www.qwant.com'),
        types.InlineKeyboardButton('📚 Gigablast', callback_data='https://www.gigablast.com'),
        types.InlineKeyboardButton('🖥️ Lycos', callback_data='https://www.lycos.com'),
        types.InlineKeyboardButton('🐕 Dogpile', callback_data='https://www.dogpile.com'),
        types.InlineKeyboardButton('🕸️ WebCrawler', callback_data='https://www.webcrawler.com'),
        types.InlineKeyboardButton('🐮 Swisscows', callback_data='https://swisscows.com'),
        types.InlineKeyboardButton('🔍 MetaGer', callback_data='https://www.metager.de'),
        types.InlineKeyboardButton('🔍 Yippy', callback_data='https://www.yippy.com'),
        types.InlineKeyboardButton('🕵️‍♂️ SearX', callback_data='https://searx.github.io'),
        types.InlineKeyboardButton('🧠 Ask', callback_data='https://www.ask.com'),
        types.InlineKeyboardButton('🟢 AOL', callback_data='https://search.aol.com')
    ]

    markup.add(*buttons)

    bot.send_message(chat_id, "Choose a search engine:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    log_user_action(message.from_user, 'Started the bot')
    send_search_keyboard(message.chat.id)

@bot.message_handler(func=lambda message: True)
def respond_to_all_messages(message):
    log_user_action(message.from_user, 'Sent a message')
    send_search_keyboard(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    log_user_action(call.from_user, f'Clicked on {call.data}')
    bot.send_message(call.message.chat.id, f"Here is your link: {call.data}")
    bot.answer_callback_query(call.id, f"Opening {call.data}")

bot.polling()
