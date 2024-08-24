import telebot
from telebot import types

# Токен, который ты получил от BotFather
TOKEN = '6939538078:AAFA7GJKasEi7VltqYXGPtCtMXIQr6E3P8A'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(row_width=3)

    # Создаем кнопки
    button1 = types.KeyboardButton('Button 1')
    button2 = types.KeyboardButton('Button 2')
    button3 = types.KeyboardButton('Button 3')
    button4 = types.KeyboardButton('Button 4')
    button5 = types.KeyboardButton('Button 5')
    button6 = types.KeyboardButton('Button 6')
    button7 = types.KeyboardButton('Button 7')
    button8 = types.KeyboardButton('Button 8')
    button9 = types.KeyboardButton('Button 9')

    # Добавляем кнопки в клавиатуру
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Welcome! Choose an option:", reply_markup=markup)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Проверяем, какая кнопка была нажата и отвечаем соответствующим сообщением
    if message.text == 'Button 1':
        bot.reply_to(message, "You pressed Button 1!")
    elif message.text == 'Button 2':
        bot.reply_to(message, "You pressed Button 2!")
    elif message.text == 'Button 3':
        bot.reply_to(message, "You pressed Button 3!")
    elif message.text == 'Button 4':
        bot.reply_to(message, "You pressed Button 4!")
    elif message.text == 'Button 5':
        bot.reply_to(message, "You pressed Button 5!")
    elif message.text == 'Button 6':
        bot.reply_to(message, "You pressed Button 6!")
    elif message.text == 'Button 7':
        bot.reply_to(message, "You pressed Button 7!")
    elif message.text == 'Button 8':
        bot.reply_to(message, "You pressed Button 8!")
    elif message.text == 'Button 9':
        bot.reply_to(message, "You pressed Button 9!")
    else:
        bot.reply_to(message, "Please choose an option from the keyboard.")

# Запуск бота
bot.polling()
