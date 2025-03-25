import telebot
from telebot import types # для указание типов
import random

API_TOKEN = '7428182829:AAEejYMls8u2KE3xqMAjJSiw1ChWJM37Org'

bot = telebot.TeleBot(API_TOKEN)


score = 0
questionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


@bot.message_handler(commands= ['start'])
def start_bot(message):
    photoLogo = open('millionaireLogo.jpg', 'rb')
    bot.send_photo(message.chat.id, photoLogo)

    ######################кнопки меню игры######################
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Правила игры")
    markup.add(btn1, btn2)
    ############################################################
    
    bot.send_message(message.chat.id, 'Добро пожаловать в игру '
                     '"Кто хочет стать миллионером?"!', reply_markup=markup) # reply_markup=markup необходимо указать для отображения кнопок в боте!
    photoLogo.close() # закрываем photoLogo


'''@bot.message_handler(content_types=['text'])
def game_bot_menu(message):
    if message.text == "Начать игру":
        #bot.send_message(message.chat.id, 'Начинаем игру!')
        game_bot_main(message)
    elif message.text == "Правила игры":
        bot.send_message(message.chat.id, 'Давайте прочитаем правила игры!')'''

def QuestionsAboutTheGame(index): # вопросы к игре
    guestions = [
        'Название крейсера, давшего бой японской эскадре у порта "Чемульпо в 1904 году?"', #0
        'Период правления Императора Николая II?', # 1
        'В каком году в Российской империи началась первая революция?', # 2
        '''Ясным  солнечным  утром  9  января  1905 г.  празднично одетые
рабочие  вместе с  жёнами  и  детьми,  неся  иконы  и портреты  царя,  двинулись
с  окраин  к  Зимнему  дворцу. В  мирном  шествии  участвовало  более  140  тыс.
человек. Но  путь  к дворцу  преградили  полиция и  войска,  которые открыли  огонь
по  демонстрантам.  По  официальным  данным,  жертвами  кровавой трагедии  стали  130 человек,
современники  говорили  о  тысячах  убитых  и  раненых.  Весть о  расстреле питерских  рабочих
вызвала гнев  и  возмущение  во  всех  слоях  общества.  Долго  копившееся  недовольство
вылилось  в  революцию.

О каком событии в истории идет речь?''', # 3
        'Кто возглавил либеральную партию "Кадеты", образовавшуюся в начале первой русской революции?', # 4
        'Кто возглавил либеральную партию "Союз 17 октября", образовавшуюся в начале первой русской революции?', # 5
        'Кто возглавил социалистическую партию "Социалисты революционеры (Эссеры)", образовавшуюся в 1902 году?', # 6
        'Кто возглавил социалистическую партию "Меньшевики", образовавшуюся в 1903 году?', # 7
        'Кто возглавил социалистическую партию "Большевики", образовавшуюся в 1903 году?', # 8
        'В результате какой революции был свергнут царь Николай II и царское правительство?', # 9
        'В результате какой революции было свергнуто Временное правительство?', # 10
        '''Политических деятель РСФСР, который c 1921 года возглавил комиссию по улучшению жизни беспризорных детей,
был во главе Всероссийской Чрезвычайной Комиссии, обеспечил восстановление, разрушенного в гражданскую войну
железнодорожного транспорта?
''', # 11
        'В каком году был принят государственный план развития электроэнергетической отрасли в Советской России после Октябрьской революции 1917 года (ГОЭЛРО)?', # 12
        'Какое событие послужило началу Гражданской войны в 1917 году?', # 13
        'В каком году началась Вторая мировая война?', # 14
        'В каком году началасть Великая отнечественная война на территории Советского союза?' # 15
        ]

    QuestionLen = len(guestions)

    return guestions[index]


def answerOptions(index):
    correctAnswers = ['Варяг', # 0
                      '1894 - 1917 гг.', # 1
                      '1905 г.', # 2
                      'Кровавое воскресенье', # 3
                      'Милюков', # 4
                      'Гучков', # 5
                      'Чернов', # 6
                      'Мартов', # 7
                      'Ленин', # 8
                      'Февральская революция', # 9
                      'Октябрьская революция', # 10
                      'Ф. Э. Дзержинский', # 11
                      '22 декабря 1920 г.', # 12
                      'Восстание Чехословацкого корпуса', # 13
                      '1939 г.', # 14
                      '1941 г.', # 15
                      ]

    print(correctAnswers[index])
    
    return correctAnswers[index]
    

def answerOptionsButton(index):
    answerOptions = [['Варяг', 'Аврора', 'Кореец', 'Диана'], # 0
                     ['1864 - 1900 гг.', '1800 - 1850 гг.', '1894 - 1917 гг.', '1894 - 1905 гг.'], # 1
                     ['1917 г.', '1905 г.', '1914 г.', '1916 г.'], # 2
                     ['Всеобщая стачка рабочих в Ростове-на-Дону', 'Всеобщая стачка рабочих на юге России', '"Обуховская оборона" рабочих в Петербурге', 'Кровавое воскресенье'], # 3
                     ['Ленин', 'Милюков', 'Гучков', 'Чернов'], # 4
                     ['Ленин', 'Милюков', 'Гучков', 'Чернов'], # 5
                     ['Ленин', 'Милюков', 'Гучков', 'Чернов'], # 6
                     ['Ленин', 'Мартов', 'Гучков', 'Чернов'], # 7
                     ['Ленин', 'Милюков', 'Гучков', 'Чернов'], # 8
                     ['Революция  с 1905-1907 гг.', 'Октябрьская революция', 'Февральская революция', 'Корниловский мятеж'], # 9
                     ['Революция  с 1905-1907 гг.', 'Октябрьская революция', 'Февральская революция', 'Корниловский мятеж'], # 10
                     ['В. И. Ленин', 'Ф. Э. Дзержинский', 'Я. М. Свердлов', 'Л. Д. Троцкий'], # 11
                     ['22 декабря 1920 г.', '22 января 1921 г.', '22 декабря 1919 г.', '22 февраля 1925 г.'], # 12
                     ['Восстание Чехословацкого корпуса', 'Кровавое воскресенье', 'Выступление Керенского — Краснова', 'Расстрел царской семьи'], # 13
                     ['1930 г.', '1939 г.', '1941 г.', '1940 г.'], # 14
                     ['1930 г.', '1939 г.', '1941 г.', '1940 г.'] # 15
                     ]

    print(answerOptions[index])

    return answerOptions[index]



#@bot.message_handler(content_types=['text'])    
def game_buttons_bot(message, guestion, buttons):
    
    '''guestion, index, QuestionLen = QuestionsAboutTheGame() # случайный выбор вопроса
    answer = answerOptions(index) # правильный ответ
    buttons = answerOptionsButton(index)  # выбор соответствующих названий для кнопок'''

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(buttons[0])
    button2 = types.KeyboardButton(buttons[1])
    button3 = types.KeyboardButton(buttons[2])
    button4 = types.KeyboardButton(buttons[3])
    markup.add(button1, button2)
    markup.add(button3, button4)
    
    bot.send_message(message.chat.id, guestion, reply_markup=markup)

    #bot.register_next_step_handler(message, game_bot_main)

    return


def question16_main(message):
    
    global score
    
    answer = answerOptions(15)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question16(message):
    guestion = QuestionsAboutTheGame(15)
    buttons = answerOptionsButton(15)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question16_main)


def question15_main(message):
    
    global score
    
    answer = answerOptions(14)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question15(message):
    guestion = QuestionsAboutTheGame(14)
    buttons = answerOptionsButton(14)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question15_main)


def question14_main(message):
    
    global score
    
    answer = answerOptions(13)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question14(message):
    guestion = QuestionsAboutTheGame(13)
    buttons = answerOptionsButton(13)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question14_main)


def question13_main(message):
    
    global score
    
    answer = answerOptions(12)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question13(message):
    guestion = QuestionsAboutTheGame(12)
    buttons = answerOptionsButton(12)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question13_main)


def question12_main(message):
    
    global score
    
    answer = answerOptions(11)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question12(message):
    guestion = QuestionsAboutTheGame(11)
    buttons = answerOptionsButton(11)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question12_main)


def question11_main(message):
    
    global score
    
    answer = answerOptions(10)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question11(message):
    guestion = QuestionsAboutTheGame(10)
    buttons = answerOptionsButton(10)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question11_main)


def question10_main(message):
    
    global score
    
    answer = answerOptions(9)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question10(message):
    guestion = QuestionsAboutTheGame(9)
    buttons = answerOptionsButton(9)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question10_main)


def question9_main(message):
    
    global score
    
    answer = answerOptions(8)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question9(message):
    guestion = QuestionsAboutTheGame(8)
    buttons = answerOptionsButton(8)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question9_main)


def question8_main(message):
    
    global score
    
    answer = answerOptions(7)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question8(message):
    guestion = QuestionsAboutTheGame(7)
    buttons = answerOptionsButton(7)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question8_main)


def question7_main(message):
    
    global score
    
    answer = answerOptions(6)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question7(message):
    guestion = QuestionsAboutTheGame(6)
    buttons = answerOptionsButton(6)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question7_main)


def question6_main(message):
    
    global score
    
    answer = answerOptions(5)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question6(message):
    guestion = QuestionsAboutTheGame(5)
    buttons = answerOptionsButton(5)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question6_main)


def question5_main(message):
    
    global score
    
    answer = answerOptions(4)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question5(message):
    guestion = QuestionsAboutTheGame(4)
    buttons = answerOptionsButton(4)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question5_main)


def question4_main(message):
    
    global score
    
    answer = answerOptions(3)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question4(message):
    guestion = QuestionsAboutTheGame(3)
    buttons = answerOptionsButton(3)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question4_main)



def question3_main(message):
    
    global score
    
    answer = answerOptions(2)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question3(message):
    guestion = QuestionsAboutTheGame(2)
    buttons = answerOptionsButton(2)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question3_main)
    

def question2_main(message):

    global score
    
    answer = answerOptions(1)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question2(message):
    guestion = QuestionsAboutTheGame(1)
    buttons = answerOptionsButton(1)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question2_main)


def question1_main(message):

    global score

    answer = answerOptions(0)
    
    if message.text == answer:
        score += 62500
        bot.send_message(message.chat.id, f'Верно! На вашем счете {score} руб.!')
    else:
        bot.send_message(message.chat.id, f'Не верно! Правильный ответ {answer}.')
        bot.send_message(message.chat.id, f'На вашем счете {score} руб.!')

    game_bot_main(message)
    

def question1(message):

    guestion = QuestionsAboutTheGame(0)
    buttons = answerOptionsButton(0)
    game_buttons_bot(message, guestion, buttons)

    bot.register_next_step_handler(message, question1_main)
    
    
def game_bot_main(message):

    global score
    global questionList
    
    try:
        questioSelection = random.choice(questionList)
        questionListLen = len(questionList)

        if questioSelection in questionList:
            questionList.remove(questioSelection)

        if questioSelection == 1:
            question1(message)
        elif questioSelection == 2:
            question2(message)
        elif questioSelection == 3:
            question3(message)
        elif questioSelection == 4:
            question4(message)
        elif questioSelection == 5:
            question5(message)
        elif questioSelection == 6:
            question6(message)
        elif questioSelection == 7:
            question7(message)
        elif questioSelection == 8:
            question8(message)
        elif questioSelection == 9:
            question9(message)
        elif questioSelection == 10:
            question10(message)
        elif questioSelection == 11:
            question11(message)
        elif questioSelection == 12:
            question12(message)
        elif questioSelection == 13:
            question13(message)
        elif questioSelection == 14:
            question14(message)
        elif questioSelection == 15:
            question15(message)
        elif questioSelection == 16:
            question16(message)

        print(questionList)
        print(questionListLen)
    except (IndexError, UnboundLocalError):
        bot.send_message(message.chat.id, 'Игра окончена!')
        bot.send_message(message.chat.id, f'Вы выйграли {score} руб.!!!!!!')
        score = 0
        questionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        start_bot(message)


@bot.message_handler(content_types=['text'])
def game_bot_menu(message):
    
    if message.text == "Начать игру":
        #bot.send_message(message.chat.id, 'Начинаем игру!')
        #game_bot(message)
        #bot.register_next_step_handler(message, game_bot_main)
        game_bot_main(message)
        #question1(message)
    elif message.text == "Правила игры":
        bot.send_message(message.chat.id, '''Игра Кто хочет стать миллионером? - это конкурс викторина,
в котором участники должны правильно ответить на ряд вопросов с несколькими вариантами ответов, чтобы перейти на следующий уровень.
Всего 16 вопросов, каждый вопрос стоит определенной суммы денег, участники не имеют никаких временных ограничений для предоставления ответа.''')

    



print(score)
bot.infinity_polling()
