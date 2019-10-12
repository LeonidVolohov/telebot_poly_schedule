import telebot
import pars_file
import datetime
import message_string

bot = telebot.TeleBot('#mytocken#')

#only work for my group
text = pars_file.get_html_file(95, 27651)
week = pars_file.schedule_week(text)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Сколько сегодня пар?')
keyboard.row('Покажи расписание на сегодня')

@bot.message_handler(commands=['start'])
def start_message(message):
    hello_string = 'Привет, ' + message.from_user.first_name + ', выбери, что ты хочешь узнать: '
    bot.send_message(message.chat.id, hello_string, reply_markup = keyboard)
    log(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'сколько сегодня пар?':
        lessons_in_day = message_string.lessons_in_day(week)
        bot.send_message(message.chat.id, lessons_in_day)
    elif message.text.lower() == 'покажи расписание на сегодня':
        today = message_string.print_today(week)
        bot.send_message(message.chat.id, today)
    else:
        bot.send_message(message.chat.id, 'Хз, о чем ты')
    log(message)

def log(message):
    print("\n ------")
    print(datetime.datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))

bot.polling(none_stop = True)
