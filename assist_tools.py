import math
import random
import wikipedia
import numexpr as ne
import datetime
import requests
import webbrowser
from bs4 import BeautifulSoup


def min_volume(eng, min):
    vol = eng.getProperty('volume')
    vol -= float(min)

    if vol < 0.1:
        vol = 0.1

    vol = round(vol, 2)
    eng.setProperty('volume', vol)
    print("Current volume:", vol, "\n")


def plus_volume(eng, plus):
    vol = eng.getProperty('volume')
    vol += float(plus)

    if vol > 1:
        vol = 1

    vol = round(vol, 2)
    eng.setProperty('volume', vol)
    print("Current volume:", vol, "\n")


def wiki(req):
    wikipedia.set_lang('ru')
    res = wikipedia.page(req)
    short_req = wikipedia.summary(req)
    short_req_talk = wikipedia.summary(req, sentences=2)

    return [res, short_req, short_req_talk]


def req_wiki(req):
    try:
        sugg = wikipedia.summary(req)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options, type(e))
        return False
    except wikipedia.exceptions.PageError as e:
        print(e)
        return False


def randm(r1, r2, f):
    if f == False:
        res = random.randint(r1, r2)
    else:
        res = random.uniform(float(r1), float(r2))
        res = round(res, 6)
    return res


def randm_f():
    res = random.random()
    return res


def is_float(n):
    n1 = float(n)
    if str(n1) == str(n):
        return True
    else:
        return False


def mute(eng, m, v):
    if m == True:
        eng.setProperty('volume', 0.00)
    else:
        if v >= 0.01:
            eng.setProperty('volume', v)
        else:
            eng.setProperty('volume', 0.01)


def solve(eq):
    solv = ne.evaluate(eq)
    return solv


def date_time():
    time = datetime.datetime.now().time().strftime("%X")
    date = datetime.datetime.now().date()
    full_time = str(datetime.datetime.now().date()) + " " + str(datetime.datetime.now().time().strftime("%X"))
    return time, date, full_time


def time_of_day():
    time = datetime.datetime.now().time()
    if datetime.time(hour=6, minute=00) <= time < datetime.time(hour=12, minute=00):
        return "Доброе утро"

    elif datetime.time(hour=12, minute=00) <= time < datetime.time(hour=18, minute=00):
        return "Добрый день"

    elif datetime.time(hour=18, minute=00) <= time < datetime.time(hour=22, minute=00):
        return "Добрый вечер"

    elif datetime.time(hour=22, minute=00) <= time:
        return "Доброй ночи"

    else:
        return "Доброй ночи"


def price_coin(coin: str):
    coin = coin.replace(" ", "-")

    URL = "https://coinmarketcap.com/currencies/" + coin.lower() + "/"
    req = requests.get(URL)

    if req.status_code == 404:
        print("Wrong coin!")
        return None, None, None, None

    soup = BeautifulSoup(req.content, "html.parser")
    price = soup.find("div", class_="priceValue").find("span").text

    try:
        percents = soup.find("span", class_="sc-15yy2pl-0 feeyND").text
    except AttributeError:
        percents = soup.find("span", class_="sc-15yy2pl-0 gEePkg").text
        plus_price = True
    else:
        plus_price = False

    return price, percents, plus_price, URL


def browser(q):
    url = "https://www.google.com/search?q=" + str(q)
    webbrowser.open(url)
