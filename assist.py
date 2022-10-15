import pyttsx3
import assist_tools as tool
import pasgen

command = "first start"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('volume', 0.25)

prev_vol = engine.getProperty("volume")

mute = False


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk(tool.time_of_day())
print(tool.time_of_day())

while True:
    command = input("Command: ")

    if command.startswith("-volume"):
        min_vol = command.split(" ")
        try:
            min_vol = float(min_vol[1])
        except (IndexError, ValueError):
            min_vol = 0.1

        engine.runAndWait()
        tool.min_volume(engine, min_vol)


    elif command.startswith("+volume"):
        max_vol = command.split(" ")
        try:
            max_vol = float(max_vol[1])
        except (IndexError, ValueError):
            max_vol = 0.1

        engine.runAndWait()
        tool.plus_volume(engine, max_vol)

    elif command == "wiki":
        wik = False
        while wik == False:
            req = input("Запрос: ")
            wik = tool.req_wiki(req)
        result = tool.wiki(req)

        print("\n")

        print(result[1], result[0].url)
        talk_res = str(result[1]).split(" ")
        talk_words = []
        for i in range(min(20, len(talk_res) - 1)):
            talk_words.append(talk_res[i])
        talk_words = "".join(talk_words)
        talk(result[2])

        print("\n")

    elif command.startswith("rand"):
        attr = command.split(" ")
        if len(attr) == 3:
            res = tool.randm(int(attr[1]), int(attr[2]), False) if tool.is_float(attr[1]) == False else tool.randm(
                float(attr[1]), float(attr[2]), True)
            print(res)
            talk(res)
        elif len(attr) == 2:
            print("Wrong attributes or command")
        else:
            res = tool.randm_f()
            print(res)
            # talk(res)

    elif command == "mute":
        prev_vol = engine.getProperty("volume")
        tool.mute(engine, True, prev_vol)
        print("Ассистент в беззвучном режиме!")

    elif command == "unmute":
        tool.mute(engine, False, prev_vol)

    elif command == ("date" or "time"):
        time, date, full_time = tool.date_time()
        short_time = time.split(":")
        print(full_time)
        talk(f"На данный момент {short_time[0]} {short_time[1]}")

    elif command.startswith("price"):
        price = command.lstrip("price ")
        prc, percents, plus_price, url = tool.price_coin(price)
        if prc and percents and plus_price != None:
            print(prc, " ", percents, end=" ")
            print("↑" if plus_price else "↓")
            print(url)
            talk(prc.strip("$,"))

    elif command.startswith("pasgen"):
        command = command.split(" ")
        if len(command) >= 2:

            try:
                print(pasgen.generate_random_password(int(command[1])))
            except TypeError:
                print("Attribute Error")
        else:
            print(pasgen.generate_random_password(8))

    elif command == "search":
        q = input("Запрос: ")
        talk("Вот что найдено по запросу " + str(q))
        tool.browser(q)

    elif command == "test":
        talk("Тест")

    else:
        try:
            solve = tool.solve(command)
        except:
            print(NameError("Wrong Command"))
        else:
            print(solve)
