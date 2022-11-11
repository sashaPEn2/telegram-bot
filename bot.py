import telebot
import parser

#main variables
TOKEN = "5150319535:AAGoWHZwzi8qFtRhP7Su_zQju4H4YwNsUu0"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()
@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я вам не понял :(')
bot.polling()
@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')
bot.polling()
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
        text = message.text
        msg = bot.send_message(chat_id, 'Сколько вам лет?')
        bot.register_next_step_handler(msg, askAge) #askSource
        isRunning = True

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет.')
    isRunning = False