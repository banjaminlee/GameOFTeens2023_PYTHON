#Нікнейм боту: @got_project_lifecellbot

import telebot
from telebot import types

bot = telebot.TeleBot('5886946602:AAHC-b5UO88-NbCMDhgH0LxoKwIMb66uEkA')
#               1  2  3  4  5  6  7  Тестовий елемент списку, щоб бот визначився чи відповіли ви на запитання
tarif_choose = [0, 0, 0, 0, 0, 0, 0, 0]
"""
1.Вільний лайф  [0]
2.Смарт лайф    [1]
3.Просто лайф   [2]
4.Platinum лайф [3]
5.Шкільний лайф [4]
6.Ґаджет        [5]
7.Смарт сім'я   [6]
"""

@bot.message_handler(commands=['start'])
def greet(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Запитання 1")
    item2 = types.KeyboardButton("Запитання 2")
    item3 = types.KeyboardButton("Запитання 3")
    item4 = types.KeyboardButton("Запитання 4")
    item5 = types.KeyboardButton("Результати")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Привіт, це {1.first_name}!\nЯ допоможу обрати Lifecell тариф, який найкраще підходить саме вам!\nНапишіть /help щоб дізнатися як користуватись ботом!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def question1(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '\t⚠️Як користуватись ботом:\
\nДля найбільш якісного результату, натискайте по черзі кнопки з написом "Запитання", відповідаючи на подані запитання. Коли закігнчили з усіма запитаннями — нажміть на кнопку "Результат" і дізнайтеся, який тариф підходить саме вам!\
\n\t⚠️Доступні команди:\
\n🔸 /start — Запуск бота\
\n\n🔸 /refresh_results — Оновити дані. \n\t‼️Обов`язково Використовуйте цю команду, якщо хочете пройти тест знову\
\n\n🔸 /help — Допомога в користуванні ботом. Список наявних команд')

@bot.message_handler(commands=['refresh_results'])
def question1(message):
    if message.chat.type == 'private':
        tarif_choose = [0, 0, 0, 0, 0, 0, 0]

@bot.message_handler(content_types=['text'])
def question1(message):
    if message.chat.type == 'private':
            if message.text == 'Запитання 1':
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1_1 = types.InlineKeyboardButton("8-10", callback_data="q1_1")
                item1_2 = types.InlineKeyboardButton("4-7", callback_data="q1_2")
                item1_3 = types.InlineKeyboardButton("1-3", callback_data="q1_3")

                markup.add(item1_1, item1_2, item1_3)

                bot.send_message(message.chat.id, "Запитання 1:\
            \nНаскільки частим ви б оцінили оцінили використання вами мобільного інтернету від 1 до 10, де:\n\
            \n1-3: Досить рідко, майже не користуюсь\n\
            \n4-7: Іноді користуюся, але кількість МБ в тарифі для мене не дуже важлива\n\
            \n8-10: Користуюсь мобільним інтернетом на постійній основі", reply_markup=markup)
                
            elif message.text == 'Запитання 2':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item2_1 = types.InlineKeyboardButton("8-10", callback_data="q2_1")
                item2_2 = types.InlineKeyboardButton("4-7", callback_data="q2_2")
                item2_3 = types.InlineKeyboardButton("1-3", callback_data="q2_3")

                markup.add(item2_1, item2_2, item2_3)

                bot.send_message(message.chat.id, "Запитання 2:\
            \nНа скільки часто ви робите дзвінки від 1 до 10, де:\n\
            \n1-3: Майже не роблю дзвінків\n\
            \n4-7: Не більше декількох дзвінків на день\n\
            \n8-10: Роблю дзвінки на постійній основі", reply_markup=markup)
                
            elif message.text == 'Запитання 3':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item3_1 = types.InlineKeyboardButton("6-10", callback_data="q3_1")
                item3_2 = types.InlineKeyboardButton("1-5", callback_data="q3_2")

                markup.add(item3_1, item3_2)

                bot.send_message(message.chat.id, "Запитання 3:\
            \nОцініть важливість для вас дзвінків на номери інших операторів від 1 до 10, де:\n\
            \n1-5: В моїх планах дзвонити тільки на номери Lifecell\n\
            \n6-10: Планую дзвонити на номери різних операторів", reply_markup=markup)

            elif message.text == 'Запитання 4':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item4_1 = types.InlineKeyboardButton("90", callback_data="q4_1")
                item4_2 = types.InlineKeyboardButton("100-150", callback_data="q4_2")
                item4_3 = types.InlineKeyboardButton("180+", callback_data="q4_3")

                markup.add(item4_1, item4_2, item4_3)

                bot.send_message(message.chat.id, "Запитання 4:\
            \nЯкою ви уявляєте приблизну ціну тарифу(В гривнях)?", reply_markup=markup)
                
            elif message.text == 'Результати':
                bot.send_message(message.chat.id, str(tarif_choose))
                if tarif_choose[0] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить тариф: [Вільний лайф]\
                    \n\Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \n\https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[1] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить тариф: [Смарт лайф]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[2] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить тариф: [Просто лайф]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[3] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить тариф: [Platinum лайф]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[4] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить тариф: [Шкільний лайф]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[5] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить один з трьох тарифів: [Ґаджет]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[6] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, 'Тест завершено. За його результатами, вам найбільше підходить один з трьох тарифів: [Ґаджет]\
                    \nБільше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/\
                    \n\nP.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')
                elif tarif_choose[7] == 0:
                    bot.send_message(message.chat.id, '‼️Помилка в обчисленні результатів\nМожливо ви дали відповіді не на всі запитання. Спробуйте пройти тест з початку')

#ОБРОБКА ВІДПОВІДЕЙ
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        #ЗАПИТАННЯ 1
        if call.data == 'q1_1':
            tarif_choose[1] +=1
            tarif_choose[3] +=1
        elif call.data == 'q1_2':
            tarif_choose[0] +=1
            tarif_choose[2] +=1
            tarif_choose[5] +=1
        elif call.data == 'q1_3':
            tarif_choose[4] +=1
        
        #ЗАПИТАННЯ 2
        if call.data == 'q2_1':
            tarif_choose[0] +=1
            tarif_choose[1] +=1
            tarif_choose[3] +=1
            tarif_choose[4] +=1
        elif call.data == 'q2_2':
            tarif_choose[2] +=1
        elif call.data == 'q2_3':
            tarif_choose[5] +=1
        
        #ЗАПИТАННЯ 3
        if call.data == 'q3_1':
            tarif_choose[0] +=1
            tarif_choose[1] +=1
            tarif_choose[2] +=1
            tarif_choose[3] +=1
            tarif_choose[6] +=1
        elif call.data == 'q3_2':
            tarif_choose[4] +=1
            tarif_choose[5] +=1

        #ЗАПИТАННЯ 4
        if call.data == 'q4_1':
            tarif_choose[0] +=2
            tarif_choose[3] +=2
            tarif_choose[6] +=2
            tarif_choose[7] +=1
        elif call.data == 'q4_2':
            tarif_choose[1] +=2
            tarif_choose[4] +=2
            tarif_choose[7] +=1
        elif call.data == 'q4_3':
            tarif_choose[5] +=2
            tarif_choose[2] +=2
            tarif_choose[7] +=1
        #remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="✔️Відповідь зараховано",
            reply_markup=None)



bot.polling(non_stop=True)