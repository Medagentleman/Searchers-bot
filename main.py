import telebot
from telebot import types
import logging

# Вставь сюда свой токен
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

bot = telebot.TeleBot(TOKEN)

# Настройка логирования
logging.basicConfig(filename='bot_activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# Функция для логирования информации о пользователе
def log_user_action(user, action):
    user_info = f"User ID: {user.id}, Name: {user.first_name}, Last Name: {user.last_name}, Username: @{user.username}, Action: {action}"
    logging.info(user_info)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    log_user_action(message.from_user, 'Started the bot')

    # Создаем инлайн-клавиатуру
    markup = types.InlineKeyboardMarkup(row_width=4)

    # Создаем 20 кнопок с callback_data, содержащими поисковые ссылки
    buttons = [
        types.InlineKeyboardButton('Google', callback_data='https://www.google.com'),
        types.InlineKeyboardButton('Yandex', callback_data='https://www.yandex.com'),
        types.InlineKeyboardButton('Bing', callback_data='https://www.bing.com'),
        types.InlineKeyboardButton('Yahoo', callback_data='https://www.yahoo.com'),
        types.InlineKeyboardButton('DuckDuckGo', callback_data='https://www.duckduckgo.com'),
        types.InlineKeyboardButton('Baidu', callback_data='https://www.baidu.com'),
        types.InlineKeyboardButton('Ask', callback_data='https://www.ask.com'),
        types.InlineKeyboardButton('AOL', callback_data='https://search.aol.com'),
        types.InlineKeyboardButton('WolframAlpha', callback_data='https://www.wolframalpha.com'),
        types.InlineKeyboardButton('Ecosia', callback_data='https://www.ecosia.org'),
        types.InlineKeyboardButton('StartPage', callback_data='https://www.startpage.com'),
        types.InlineKeyboardButton('Qwant', callback_data='https://www.qwant.com'),
        types.InlineKeyboardButton('Gigablast', callback_data='https://www.gigablast.com'),
        types.InlineKeyboardButton('Lycos', callback_data='https://www.lycos.com'),
        types.InlineKeyboardButton('Dogpile', callback_data='https://www.dogpile.com'),
        types.InlineKeyboardButton('WebCrawler', callback_data='https://www.webcrawler.com'),
        types.InlineKeyboardButton('Swisscows', callback_data='https://swisscows.com'),
        types.InlineKeyboardButton('MetaGer', callback_data='https://www.metager.de'),
        types.InlineKeyboardButton('Yippy', callback_data='https://www.yippy.com'),
        types.InlineKeyboardButton('SearX', callback_data='https://searx.github.io')
    ]

    # Добавляем кнопки в клавиатуру
    markup.add(*buttons)

    # Отправляем сообщение с инлайн-клавиатурой
    bot.send_message(message.chat.id, "Choose a search engine:", reply_markup=markup)


# Обработчик нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    log_user_action(call.from_user, f'Clicked on {call.data}')

    # Отправляем пользователю ссылку
    bot.send_message(call.message.chat.id, f"Here is your link: {call.data}")

    # Ответ на запрос (необязательно, но оставим)
    bot.answer_callback_query(call.id, f"Opening {call.data}")


# Запуск бота
bot.polling()
