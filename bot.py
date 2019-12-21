# TODO: separate api_link, token from code for easier unified access

import telebot
from telebot import apihelper, types
import datetime
import sys
sys.path.insert(1, '/*MyPath*/code/utils/')
sys.path.insert(2, '/*MyPath*/code/web_tools/')

import group_funcs
import schedule_funcs
import initializer

api_link = 'http://ruz.spbstu.ru/api/v1/ruz'

apihelper.proxy = {'https': 'https://167.172.140.184:3128'}
bot = telebot.TeleBot('<TOKEN>')
KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
KEYBOARD.row('Сколько сегодня пар?')
KEYBOARD.row('Расписание на сегодня')
KEYBOARD.row('Расписание на неделю')

group_funcs.GROUP_IDS = initializer.get_groups(api_link)
print('bot is UP!')


@bot.message_handler(commands=['start'])
def start_communication(message):
    welcome_message = '\n'.join(('Привет, ' + message.from_user.first_name + '. Я могу помочь узнать расписание.',
                                 'Для начала укажи свою группу. Сделать это можно с помощью команды "/set_group <номер группы>".',
                                 'Например "/set_group 3530904/70101". Ты всегда сможешь изменить свой выбор.'))
    bot.send_message(message.chat.id, welcome_message)
    log(message)


@bot.message_handler(commands=['set_group'])
def get_group(message):
    try:
        group = group_funcs.parse_group_from_user(message.text)
        group_funcs.remember_relation(user_id=message.from_user.id, group=group)
        update_message = 'Отлично, твоя группа обновлена'
        keyboard = KEYBOARD
    except ValueError:
        update_message = '\n'.join(('Мне не удалось распознать номер группы.',
                                    'Попробуй ещё раз с помощью "/set_group <номер группы>".',
                                    'Например "/set_group 3530904/70101".'))
        keyboard = types.ReplyKeyboardRemove()
    bot.send_message(chat_id=message.chat.id,
                     text=update_message, reply_markup=keyboard)
    log(message)


@bot.message_handler(content_types=['text'])
def process_request(message):
    try:
        user_schedule = schedule_funcs.personal_schedule(message.from_user.id)
        if message.text.lower() == 'сколько сегодня пар?':
            response_message = user_schedule.count_lessons_today()
        elif message.text.lower() == 'расписание на сегодня':
            response_message = user_schedule.for_today()
        elif message.text.lower() == 'расписание на неделю':
            response_message = user_schedule.for_current_week()
        else:
            response_message = '\n'.join('Ты просишь от меня слишком многого, я этого ещё не умею!')
    # May be thrown if user is unknown yet
    except KeyError:
        response_message = '\n'.join(('Ты указал неверный номер группы. Я не могу её распознать',
                                        'Укажи её, пожалуйста, через "/set_group <номер группы>"'))
    except SyntaxError:
        response_message = '\n'.join(('Ты неправильно написал номер группы.', 
                                        'Укажи её, пожалуйста, через "/set_group <номер группы>"'))
    bot.send_message(message.chat.id, response_message)
    log(message)


def log(message):
    print('\n ------')
    print(datetime.datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nТекст = {3}'.format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id), message.text))


bot.polling(none_stop=True)
