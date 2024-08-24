import telebot
from telebot import types

# Вставь сюда свой токен
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем инлайн-клавиатуру
    markup = types.InlineKeyboardMarkup(row_width=3)

    # Создаем кнопки с URL
    button1 = types.InlineKeyboardButton('Google', url='https://www.google.com')
    button2 = types.InlineKeyboardButton('Yandex', url='https://www.yandex.com')
    button3 = types.InlineKeyboardButton('Bing', url='https://www.bing.com')
    button4 = types.InlineKeyboardButton('Yahoo', url='https://www.yahoo.com')
    button5 = types.InlineKeyboardButton('DuckDuckGo', url='https://www.duckduckgo.com')
    button6 = types.InlineKeyboardButton('Baidu', url='https://www.baidu.com')
    button7 = types.InlineKeyboardButton('Ask', url='https://www.ask.com')
    button8 = types.InlineKeyboardButton('AOL', url='https://search.aol.com')
    button9 = types.InlineKeyboardButton('WolframAlpha', url='https://www.wolframalpha.com')
    button10 = types.InlineKeyboardButton('StartPage', url='https://www.startpage.com')
    button11 = types.InlineKeyboardButton('Qwant', url='https://www.qwant.com')
    button12 = types.InlineKeyboardButton('Swisscows', url='https://swisscows.com')
    button13 = types.InlineKeyboardButton('Ecosia', url='https://www.ecosia.org')
    button14 = types.InlineKeyboardButton('Mojeek', url='https://www.mojeek.com')
    button15 = types.InlineKeyboardButton('MetaGer', url='https://www.metager.de')
    button16 = types.InlineKeyboardButton('Dogpile', url='https://www.dogpile.com')
    button17 = types.InlineKeyboardButton('Lukol', url='https://www.lukol.com')
    button18 = types.InlineKeyboardButton('Gibiru', url='https://gibiru.com')
    button19 = types.InlineKeyboardButton('Searx', url='https://searx.me')
    button20 = types.InlineKeyboardButton('Gigablast', url='https://www.gigablast.com')

    # Добавляем кнопки в клавиатуру
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    markup.add(button11, button12, button13, button14, button15, button16, button17, button18, button19, button20)

    # Отправляем сообщение с инлайн-клавиатурой
    bot.send_message(message.chat.id, "Choose a search engine:", reply_markup=markup)


# Запуск бота
bot.polling()
