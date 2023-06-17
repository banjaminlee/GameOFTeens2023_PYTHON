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
    item5 = types.KeyboardButton("Запитання 5")
    item6 = types.KeyboardButton("Результати")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Привіт, це бот <b>{1.first_name}</b>🗼\nЯ допоможу обрати Lifecell тариф, який найкраще підходить саме вам!\nНапишіть /help щоб дізнатися як користуватись ботом!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def question1(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '\t⚠️Як користуватись ботом:\
\nДля найбільш якісного результату, натискайте по черзі кнопки з написом "Запитання", відповідаючи на подані запитання. Коли закінчили з усіма запитаннями — нажміть на кнопку "Результат" і дізнайтеся, який тариф підходить саме вам!\
\n\t⚠️Доступні команди:\
\n🔸 /start — Запуск бота\
\n🔸 /help — Допомога в користуванні ботом; список наявних команд')

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
            \n«📱Я — губка, яка поглинає інформацію, особливо в інтернеті! Люблю позалипати в соц.мережах, онлайн 24/7. Часто користуюсь інтернетом!»\n\
            \nОцініть, чи підходите ви під цей опис за шкалою від 1 до 10, де: \
            \n1-3: Ні, це повна протилежність мені!\n\
            \n4-7: Користуюся мобільним інтернетом в міру! 50/50\n\
            \n8-10: Це точно про мене!", reply_markup=markup)
                
            elif message.text == 'Запитання 2':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item2_1 = types.InlineKeyboardButton("8-10", callback_data="q2_1")
                item2_2 = types.InlineKeyboardButton("4-7", callback_data="q2_2")
                item2_3 = types.InlineKeyboardButton("1-3", callback_data="q2_3")

                markup.add(item2_1, item2_2, item2_3)

                bot.send_message(message.chat.id, "Запитання 2:\
            \n«☎️Я ділова людина: постійно роблю дзвінки, домовляюсь про зустрічі.\nТелефон для мене — це в першу чергу предмет комунікації»\n\
            \nОцініть, наскільки добре ці речення описують вас за шкалою від 1 до 10, де:\
            \n1-3: Зовсім не про мене, рідко роблю дзвінки\n\
            \n4-7: Не можу визначитись, 50/50\n\
            \n8-10: Так, це про мене! Постійно роблю дзвінки", reply_markup=markup)
                
            elif message.text == 'Запитання 3':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item3_1 = types.InlineKeyboardButton("1", callback_data="q3_1")
                item3_2 = types.InlineKeyboardButton("2", callback_data="q3_2")

                markup.add(item3_1, item3_2)

                bot.send_message(message.chat.id, "Запитання 3:\
            \n📞Чи в ваших планах дзвонити на номери інших операторів?\n\
            \n1. Всі знайомі вже підключились до Lifecell! Планую дзвонити в основному на номери цього оператора\n\
            \n2. Планую дзвонити на номери різних операторів", reply_markup=markup)

            elif message.text == 'Запитання 4':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item4_1 = types.InlineKeyboardButton("90", callback_data="q4_1")
                item4_2 = types.InlineKeyboardButton("100-150", callback_data="q4_2")
                item4_3 = types.InlineKeyboardButton("180+", callback_data="q4_3")

                markup.add(item4_1, item4_2, item4_3)

                bot.send_message(message.chat.id, "Запитання 4:\
            \n💸Якою ви уявляєте приблизну ціну тарифу(В гривнях)?", reply_markup=markup)
                
            elif message.text == 'Запитання 5':
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5_1 = types.InlineKeyboardButton("1", callback_data="q5_1")
                item5_2 = types.InlineKeyboardButton("2", callback_data="q5_2")

                markup.add(item5_1, item5_2)

                bot.send_message(message.chat.id, "Запитання 5:\
            \n👨‍👩‍👧‍👦Чи цікавить вас тариф зі спільним використанням пакетом послуг?\n\
            \n1: Ні, хочу тариф для власного використання!\n\
            \n2: Так, мене цікавить такий тариф!", reply_markup=markup)
                
            elif message.text == 'Результати':
                if tarif_choose[0] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить тариф: [Вільний лайф]\
                    \nВід 180грн / 4 тижні\
                    \n\n💻Інтернет: Безліміт\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◽️] 100%\
                    \n\n📱Дзвінки: 1600хв\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◼️] 90%\
                    \nДзвінки на всі номери по Україні (міські, мобільні, lifecell)\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \n\https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[1] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить тариф: [Смарт лайф]\
                    \nВід 120грн / 4 тижні\
                    \n\n💻Інтернет: 25ГБ\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◼️◼️] 80%\
                    \n\n📱Дзвінки: 800хв\
                    \n[◽️◽️◽️◽️◽️◽️◽️◼️◼️◼️] 70%\
                    \nДзвінки на всі мобільні номери по Україні (вкл. lifecell)\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[2] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить тариф: [Просто лайф]\
                    \nВід 90грн / 4 тижні\
                    \n\n💻Інтернет: 8 ГБ\
                    \n[◽️◽️◽️◼️◼️◼️◼️◼️◼️◼️] 30%\
                    \n\n📱Дзвінки: 300 хв\
                    \n[◽️◽️◽️◼️◼️◼️◼️◼️◼️◼️] 30%\
                    \nДзвінки на всі мобільні номери по Україні (вкл. lifecell)\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[3] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить тариф: [Platinum лайф]\
                    \nВід 250грн / 4 тижні\
                    \n\n💻Інтернет: Безліміт\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◽️] 100%\
                    \n\n📱Дзвінки: 3000 хв\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◼️] 90%\
                    \nДзвінки на всі номери по Україні (міські, мобільні, lifecell)\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[4] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить тариф: [Шкільний лайф]\
                    \nВід 150грн / 4 тижні\
                    \n\n💻Інтернет: 7 ГБ\
                    \n[◽️◽️◽️◼️◼️◼️◼️◼️◼️◼️] 30%\
                    \n\n📱Дзвінки: Безліміт\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◽️] 100%\
                    \nДзвінки на lifecell\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[5] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить один з трьох тарифів: [Ґаджет]\
                    \nВід 90грн / 12 тижнів\
                    \n\n💻Інтернет: від 150 МБ до безліміту\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◽️◽️] 100%\
                    \n\n📱Дзвінки: від 15 хв до 50 хв\
                    \n[◽️◼️◼️◼️◼️◼️◼️◼️◼️◼️] 10%\
                    \nДзвінки на lifecell, хв/день\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/')

                elif tarif_choose[6] == max(tarif_choose) and tarif_choose[7] != 0:
                    bot.send_message(message.chat.id, '🚀Тест завершено. За його результатами, вам найбільше підходить один з трьох тарифів: [Смарт Сім`я]\
                    \nвід 375 грн / 4 тижні\
                    \n\n💻Інтернет: від 20 ГБ до 50 ГБ\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◼️◼️] 80%\
                    \n\n📱Дзвінки: від 500 хв до 1500 хв\
                    \n[◽️◽️◽️◽️◽️◽️◽️◽️◼️◼️] 80%\
                    \nДзвінки на інші міські та мобільні номери по Україні\
                    \n\n🗂Більше про цей тариф ви зможете дізнатися за посиланням:\
                    \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/\
                    \n\n🔍P.S. Якщо ви не впевнені, що це саме той тариф, який підходить вам найбільше, ви завжди можете обрати інший на нашому сайті:\
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
            tarif_choose[2] +=999
            tarif_choose[5] +=999
        elif call.data == 'q4_2':
            tarif_choose[1] +=999
            tarif_choose[4] +=999
        elif call.data == 'q4_3':
            tarif_choose[0] +=999
            tarif_choose[3] +=999
            tarif_choose[6] +=999
        #ЗАПИТАННЯ 5
        if call.data == 'q5_1':
            tarif_choose[0] +=1
            tarif_choose[1] +=1
            tarif_choose[2] +=1
            tarif_choose[3] +=1
            tarif_choose[4] +=1
            tarif_choose[5] +=1
            tarif_choose[7] +=1
        elif call.data == 'q5_2':
            tarif_choose[6] +=9999
            tarif_choose[7] +=1
        #remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="✔️Відповідь зараховано",
            reply_markup=None)



bot.polling(non_stop=True)
