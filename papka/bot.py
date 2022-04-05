import telebot
import datetime
from pyowm import OWM
from pyowm.utils.config import get_default_config
import time
import math
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from telebot import types


u1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
u2 = "/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
useragent = u1 + u2

novosti = "https://ria.ru/economy/"
novosti2 = Request(novosti, headers={'User-Agent': useragent})
f4 = urlopen(novosti2, timeout=10).read()
soup4 = BeautifulSoup(f4, "lxml")

ua1 = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D"                    #юань
ua2 = "1%81+%D1%8E%D0%B0%D0%BD%D1%8F&oq=rehc+.fyz&aqs=chrome.1.69i"
ua3 = "57j0i10i131i433j0i10j0i10i433j0i10l6.5111j1j7&sourceid=chrome&ie=UTF-8"
siteuan = ua1 + ua2 + ua3
siteuan2 = Request(siteuan, headers={'User-Agent': useragent})
f3 = urlopen(siteuan2, timeout=5).read()
soup3 = BeautifulSoup(f3, "lxml")
uani = str(soup3.find("span", class_="DFlfde SwHCTb").text)


e1 = "https://www.google.com/search?q=%D0%BA%D1%83%D"                           #евро
e2 = "1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=rehc+td&aq"
e3 = "s=chrome.1.69i57j0i10l5j0i10i457j0i402j0i10l2.4598j1j7&sourceid=chrome&ie=UTF-8"
site3 = e1 + e2 + e3
site4 = Request(site3, headers={'User-Agent': useragent})
f2 = urlopen(site4, timeout=5).read()
soup2 = BeautifulSoup(f2, "lxml")
euro = str(soup2.find("span", class_="DFlfde SwHCTb").text)


a1 = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0"       #доллар
a2 = "%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc&aqs=chrome.1.69i57j0i67i131i433"
a3 = "l3j0i67l2j0i67i131i433l3j0i67.3124j1j7&sourceid=chrome&ie=UTF-8"
site = a1 + a2 + a3
site2 = Request(site, headers={'User-Agent': useragent})
f = urlopen(site2, timeout=5).read()
soup = BeautifulSoup(f, "lxml")
dollar = str(soup.find("span", class_="DFlfde SwHCTb").text)


config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = OWM('75e6e77d3dd966699ae9ce85924c0168')
mgr = owm.weather_manager()
place = 'Воронеж'
observation = mgr.weather_at_place(place)
w = observation.weather
s = str(observation.weather.detailed_status)
l = str(w.wind())
speed = str(w.wind()["speed"])
print(speed)
pont = str(w.humidity)
print(s)
temp = str(w.temperature("celsius")["temp_min"])
print(temp)
temp2 = math.ceil(float(temp))
temp = str(temp2)

tim = datetime.datetime.now()
bot = telebot.TeleBot("Your Token")  #Enter your token


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/Возможности")
    markup.add(item1)
    bot.send_message(message.chat.id, "Привет, я ПЕПЕ!. Бот созданный для информирования в плане погоды и новостей. Создан для ускорения потребленя информации.\nЕсли хочешь узнать о мне больше, то нажми на кнопку 'Возможности'", reply_markup=markup)
    id = str(message.from_user.first_name)
    txt = str(message.text)
    print(id,"отправил боту следующее сообщение: '",txt,"'")

@bot.message_handler(commands=['Возможности'])
def help(message):
    sti5 = open('info.webp', 'rb')
    bot.send_sticker(message.chat.id, sti5)    
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonpog = types.KeyboardButton("/Погода🌧")
    buttonkurs = types.KeyboardButton("/Курс_валют💰")
    buttonews = types.KeyboardButton("/Новости📰")
    buttonNastroika = types.KeyboardButton("/Запустить_цикл_ежедневных_сообщений📬")
    markup1.add(buttonpog, buttonkurs, buttonews, buttonNastroika)
    bot.send_message(message.chat.id, 'Вот, что я могу:\n \n1. Показывать погоду;\n2. Показывать курс доллара, евро, юаня;\n3. Показывать верные новости;\n4. Всё из выше перечисленного присылать вам в шесть утра', reply_markup=markup1)
    id = str(message.from_user.first_name)
    txt = str(message.text)
    print(id,"отправил боту следующее сообщение: '",txt,"'")

@bot.message_handler(commands=['Погода🌧'])
def pogoda(message):
    bot.send_message(message.chat.id, 'В Воронеже сейчас ' + s + ' \nСегодня минимальная температура примерно: ' + temp + ' градусов цельсия\nВлажность около: ' + pont +'%\nСкорость ветра: ' + speed + ' м/с' + l.format(message.from_user, bot.get_me()))
    bot.send_message(message.chat.id, 'В Воронеже сейчас ' + s + ' \nСегодня минимальная температура примерно: ' + temp + ' градусов цельсия\nВлажность около: ' + pont +'%\nСкорость ветра: ' + speed + ' м/с'.format(message.from_user, bot.get_me()))
    if float(temp) < 5:
        sti1 = open('zima.webp', 'rb')
        bot.send_message(message.chat.id, 'Сегодня холодно, оденься хорошо, чтобы не замёрзнуть!'.format(message.from_user, bot.get_me()))
        bot.send_sticker(message.chat.id, sti1)
    elif 5 <= float(temp) <= 15:
        sti2 = open('osen.webp', 'rb')
        bot.send_message(message.chat.id, 'Сегодня немного холодно, оденься потеплее!'.format(message.from_user, bot.get_me()))
        bot.send_sticker(message.chat.id, sti2)
    elif 15 < float(temp) < 30:
        sti3 = open('teplo.webp', 'rb')
        bot.send_message(message.chat.id, 'Сегодня умеренно, одевайся полегче'.format(message.from_user, bot.get_me()))
        bot.send_sticker(message.chat.id, sti3)
    elif float(temp) >= 30:
        sti4 = open('zhara.webp', 'rb')
        bot.send_message(message.chat.id, 'Сегодня жарко, пей больше прохладных напитков и одевайся очегь легко!'.format(message.from_user, bot.get_me()))
        bot.send_sticker(message.chat.id, sti4)   

@bot.message_handler(commands=['Курс_валют💰'])
def kursvsego(message):
    bot.send_message(message.chat.id, "Рубль наа сегодня: \n\nКурс доллара: " + dollar + "₽✔\nКурс евро: " + euro + "₽" + '✔\nКурс юаня: ' + uani + "₽✔".format(message.from_user, bot.get_me()))
    id = str(message.from_user.first_name)
    txt = str(message.text)
    print(id,"отправил боту следующее сообщение: '",txt,"'")

@bot.message_handler(commands=['Запустить_цикл_ежедневных_сообщений📬'])
def nastroika(message):
        
    bot.send_message(message.chat.id, 'Теперь, каждый раз в шесть часов утра, я буду вам присылать сведенья о погоде'.format(message.from_user, bot.get_me()))

    while True:
        @bot.message_handler(content_types=['Text'])
        def pog(temp,s,l,pont,speed):
            temp = math.ceil(float(temp))
            temp = str(temp)
            bot.send_message(message.chat.id, 'В Воронеже сейчас ' + s + ' \nСегодня минимальная температура примерно: ' + temp + ' градусов цельсия\nВлажность около: '+ pont +'%\nСкорость ветра: ' + speed + ' м/с' + l.format(message.from_user, bot.get_me()))
            if float(temp) < 5:
                sti1 = open('zima.webp', 'rb')
                bot.send_message(message.chat.id, 'Сегодня холодно, оденься хорошо, чтобы не замёрзнуть!'.format(message.from_user, bot.get_me()))
                bot.send_sticker(message.chat.id, sti1)
            elif float(temp) >= 5 and float(temp) <= 15:
                sti2 = open('osen.webp', 'rb')
                bot.send_message(message.chat.id, 'Сегодня немного холодно, оденься потеплее!'.format(message.from_user, bot.get_me()))
                bot.send_sticker(message.chat.id, sti2)
            elif float(temp) > 15 and float(temp) < 30:
                sti3 = open('teplo.webp', 'rb')
                bot.send_message(message.chat.id, 'Сегодня умеренно, одевайся полегче'.format(message.from_user, bot.get_me()))
                bot.send_sticker(message.chat.id, sti3)
            elif float(temp) >= 30:
                sti4 = open('zhara.webp', 'rb')
                bot.send_message(message.chat.id, 'Сегодня жарко, пей больше прохладных напитков и одевайся очегь легко!'.format(message.from_user, bot.get_me()))
                bot.send_sticker(message.chat.id, sti4)
            print('Конец прикола! Ура!')    
            return()
            
        g = 0
        tim = datetime.datetime.now()

        def Text(a,b,c,temp,s,l,pont,speed,dollar):
            g = 0
            vremya(a, b, c, g)
            print('Выключатель равен',vr(g))
            if vr(g) == 1:
                pog(temp,s,l,pont,speed)
            time.sleep(1)
            owm = OWM('75e6e77d3dd966699ae9ce85924c0168')
            mgr = owm.weather_manager()
            place = 'Воронеж'
            observation = mgr.weather_at_place(place)
            w = observation.weather
            s = str(observation.weather.detailed_status)
            l = str(w.wind())
            speed = str(w.wind()["speed"])
            pont = str(w.humidity)
            temp = str(w.temperature("celsius")["temp"])
            kurs(dollar)
            news2()

            chisla(a,b,c,1,temp,s,l,pont,speed,dollar)

        @bot.message_handler(content_types=['Text'])
        def news2():
            novosti = "https://ria.ru/economy/"
            novosti2 = Request(novosti, headers={'User-Agent': useragent})
            f4 = urlopen(novosti2, timeout=10).read()
            soup4 = BeautifulSoup(f4, "lxml")
            soderzhanie = soup4.find_all("a", class_="list-item__title color-font-hover-only")
            massive = []
            for item in soderzhanie:
                item_text = item.text
                item_url = item.get("href")
                massive.append(item_text)
            bot.send_message(message.chat.id, '\nВот свежие новости с сайта РИА: \n\n' + '✅\n\n'.join(massive) .format(message.from_user, bot.get_me()))


        @bot.message_handler(content_types=['Text'])
        def kurs(dollar):
            u1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
            u2 = "/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
            useragent = u1 + u2

            ua1 = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D"                    #юань
            ua2 = "1%81+%D1%8E%D0%B0%D0%BD%D1%8F&oq=rehc+.fyz&aqs=chrome.1.69i"
            ua3 = "57j0i10i131i433j0i10j0i10i433j0i10l6.5111j1j7&sourceid=chrome&ie=UTF-8"
            siteuan = ua1 + ua2 + ua3
            siteuan2 = Request(siteuan, headers={'User-Agent': useragent})
            f3 = urlopen(siteuan2, timeout=5).read()
            soup3 = BeautifulSoup(f3, "lxml")
            uani = str(soup3.find("span", class_="DFlfde SwHCTb").text)
            print(uani)

            e1 = "https://www.google.com/search?q=%D0%BA%D1%83%D"                           #евро
            e2 = "1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=rehc+td&aq"
            e3 = "s=chrome.1.69i57j0i10l5j0i10i457j0i402j0i10l2.4598j1j7&sourceid=chrome&ie=UTF-8"
            site3 = e1 + e2 + e3
            site4 = Request(site3, headers={'User-Agent': useragent})
            f2 = urlopen(site4, timeout=5).read()
            soup2 = BeautifulSoup(f2, "lxml")
            euro = str(soup2.find("span", class_="DFlfde SwHCTb").text)
            print(euro)

            a1 = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0"       #доллар
            a2 = "%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc&aqs=chrome.1.69i57j0i67i131i433"
            a3 = "l3j0i67l2j0i67i131i433l3j0i67.3124j1j7&sourceid=chrome&ie=UTF-8"
            site = a1 + a2 + a3
            site2 = Request(site, headers={'User-Agent': useragent})
            f = urlopen(site2, timeout=5).read()
            soup = BeautifulSoup(f, "lxml")
            dollar = str(soup.find("span", class_="DFlfde SwHCTb").text)
            print(dollar)
            bot.send_message(message.chat.id, "Рубль наа сегодня: \n\nКурс доллара: " + dollar + "₽✔\nКурс евро:" + euro + "₽" + '✔\nКурс юаня: ' + uani + "₽✔".format(message.from_user, bot.get_me()))

            
        def vr(g):
            g = 1
            return g

        def vremya(a, b, c, g):
            print('Начало временного цикла')
            while True:
                tim = datetime.datetime.now()
                if (int(tim.hour) == a) and (int(tim.minute) == b) and (int(tim.second) == c):
                    print("Временной цикл завершён")
                    break
                vr(g)
            print('Выключатель равен ',g)
            return g

        def chisla(a,b,c,x,temp,s,l,pont,speed,dollar):
            print('Прикол начался')
            if  x == 0:
                a = int(input("Введи часы: "))
                b = int(input("Введи минуты: "))
                c = int(input("Введи секунды: "))
                Text(6,0,0,temp,s,l,pont,speed,dollar)
            else:
                Text(a,b,c,temp,s,l,pont,speed,dollar)
                print('Цикл начинается снова')
        
        chisla(0,0,0,0,temp,s,l,pont,speed,dollar)

@bot.message_handler(commands=['Новости📰'])
def news(message):
    novosti = "https://ria.ru/economy/"
    novosti2 = Request(novosti, headers={'User-Agent': useragent})
    f4 = urlopen(novosti2, timeout=10).read()
    soup4 = BeautifulSoup(f4, "lxml")
    soderzhanie = soup4.find_all("a", class_="list-item__title color-font-hover-only")
    massive = []
    for item in soderzhanie:
        item_text = item.text
        item_url = item.get("href")
        massive.append(item_text)
    bot.send_message(message.chat.id, '\nВот свежие новости с сайта РИА: \n\n' + '✅\n\n'.join(massive) .format(message.from_user, bot.get_me()))
    id = str(message.from_user.first_name)
    txt = str(message.text)
    print(id,"отправил боту следующее сообщение: '",txt,"'")

@bot.message_handler(content_types=['text'])
def informacia(message):
    id = str(message.from_user.first_name)
    txt = str(message.text)
    print(id,"отправил боту следующее сообщение: '",txt,"'")


bot.polling(none_stop=True)